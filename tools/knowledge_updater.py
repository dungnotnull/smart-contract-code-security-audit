# -*- coding: utf-8 -*-
"""
knowledge_updater.py — self-improving crawl pipeline for Skill #140
(Security Audit for Smart Contracts / Source Code (zero-day), cluster: software-devops).

Pattern (per CLAUDE.md):
  1. crawl4ai -> fetch latest papers/standards from domain sources
  2. WebSearch -> latest news/reports from authoritative domain sources
  3. Parse -> title, authors, date, DOI/URL, abstract, key findings
  4. Score -> rank by recency + domain-keyword relevance
  5. Append -> add scored entries to SECOND-KNOWLEDGE-BRAIN.md (date-stamped)
  6. Deduplicate -> skip entries already present (DOI/URL hash)

Recommended schedule: weekly cron.
Graceful degradation: if crawl4ai / network is unavailable, log and exit 0
so the skill keeps working off the existing knowledge base.
"""

import os
import re
import sys
import json
import hashlib
import datetime
import logging
from typing import List, Dict, Set, Optional
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Configuration
ARXIV_CATEGORIES = ["cs.CR", "cs.SE", "cryptology"]
WEB_SOURCES = [
    "https://swcregistry.io",
    "https://owasp.org",
    "https://cwe.mitre.org",
    "https://consensys.io/diligence",
    "https://first.org/cvss/calculator/4.0"
]
SEARCH_QUERIES = [
    "smart contract vulnerability reentrancy 2026",
    "zero day disclosure CVE",
    "defi exploit post-mortem",
    "static analysis fuzzing solidity",
    "smart contract security audit 2026",
    "blockchain vulnerability detection"
]

BRAIN = os.path.join(os.path.dirname(__file__), "..", "SECOND-KNOWLEDGE-BRAIN.md")
RELEVANCE_KEYWORDS = [w for query in SEARCH_QUERIES for w in query.split()]

# File paths
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
OS_STATE_FILE = os.path.join(LOG_DIR, "knowledge_updater_state.json")


def ensure_directories():
    """Ensure log directory exists."""
    os.makedirs(LOG_DIR, exist_ok=True)


def load_state() -> Dict:
    """Load previous state for incremental updates."""
    if os.path.exists(OS_STATE_FILE):
        try:
            with open(OS_STATE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Could not load state file: {e}")
    return {"last_run": None, "processed_urls": [], "run_count": 0}


def save_state(state: Dict):
    """Save current state for next run."""
    ensure_directories()
    try:
        with open(OS_STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        logger.warning(f"Could not save state file: {e}")


def hash_url(url: str) -> str:
    """
    Generate a consistent hash for a URL.
    Uses SHA-256 and returns first 16 characters for deduplication.
    """
    if not url:
        return ""
    # Normalize URL for consistent hashing
    normalized = url.lower().strip()
    # Remove fragments and common query parameters
    parsed = urlparse(normalized)
    clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    return hashlib.sha256(clean_url.encode("utf-8")).hexdigest()[:16]


def extract_existing_hashes(text: str) -> Set[str]:
    """
    Extract all existing hashes from the knowledge brain file.
    Format: <!--hash:XXXXXXXX-->
    """
    return set(re.findall(r"<!--hash:([0-9a-f]{16})-->", text))


def calculate_relevance_score(title: str, abstract: str) -> float:
    """
    Calculate relevance score based on keyword matches.
    Returns a float between 0 and 1.
    """
    if not title and not abstract:
        return 0.0

    blob = (title + " " + (abstract or "")).lower()
    hits = sum(1 for keyword in RELEVANCE_KEYWORDS if keyword.lower() in blob)
    max_possible = len(RELEVANCE_KEYWORDS)
    return hits / max(1, max_possible)


def fetch_with_crawl4ai() -> List[Dict]:
    """
    Fetch entries using crawl4ai library.
    Returns list of entry dicts with metadata.
    """
    entries = []
    try:
        from crawl4ai import WebCrawler

        logger.info("Initializing crawl4ai...")
        crawler = WebCrawler(
            headless=True,
            browser_type="chromium",
            verbose=False
        )

        try:
            crawler.warmup()
            logger.info("Crawl4ai warmed up successfully")
        except Exception as e:
            logger.warning(f"Crawl4ai warmup failed: {e}")
            # Continue anyway - crawler may still work

        # Fetch from ArXiv
        for category in ARXIV_CATEGORIES:
            try:
                code = category.split()[0]
                url = f"https://arxiv.org/list/{code}/recent"
                logger.info(f"Fetching ArXiv category: {category}")

                result = crawler.run(url=url)
                if result:
                    markdown = getattr(result, "markdown", "") or ""
                    if markdown.strip():
                        new_entries = parse_arxiv_feed(markdown, url)
                        logger.info(f"Parsed {len(new_entries)} entries from {category}")
                        entries.extend(new_entries)
                else:
                    logger.warning(f"No result from {url}")
            except Exception as e:
                logger.warning(f"Failed to fetch ArXiv {category}: {e}")

        # Fetch from web sources
        for source_url in WEB_SOURCES:
            try:
                logger.info(f"Fetching web source: {source_url}")
                result = crawler.run(url=source_url)

                if result:
                    markdown = getattr(result, "markdown", "") or ""
                    if markdown.strip():
                        entries.append({
                            "title": f"Update scan: {source_url}",
                            "authors": "N/A",
                            "year": str(datetime.date.today().year),
                            "venue": urlparse(source_url).netloc,
                            "url": source_url,
                            "abstract": markdown[:800] + "..." if len(markdown) > 800 else markdown,
                            "relevance": 0.5  # Default relevance for source scans
                        })
                        logger.info(f"Added entry for {source_url}")
                else:
                    logger.warning(f"No result from {source_url}")
            except Exception as e:
                logger.warning(f"Failed to fetch {source_url}: {e}")

        logger.info(f"Crawl4ai completed: {len(entries)} total entries fetched")

    except ImportError:
        logger.warning("crawl4ai not installed; skipping live crawl")
    except Exception as e:
        logger.warning(f"Crawl4ai unavailable: {e}")

    return entries


def parse_arxiv_feed(markdown: str, source_url: str) -> List[Dict]:
    """
    Parse ArXiv RSS/list page for paper entries.
    Extracts paper IDs and constructs entry metadata.
    """
    entries = []
    current_year = str(datetime.date.today().year)

    # Pattern to match ArXiv paper IDs (e.g., arXiv:2401.12345)
    pattern = r"arXiv:(\d{4}\.\d{4,5})"
    matches = re.finditer(pattern, markdown, re.IGNORECASE)

    for match in matches:
        paper_id = match.group(1)
        entries.append({
            "title": f"ArXiv {paper_id}",
            "authors": "Various",
            "year": current_year,
            "venue": "arXiv",
            "url": f"https://arxiv.org/abs/{paper_id}",
            "abstract": f"Paper ID {paper_id} from {current_year}",
            "relevance": 0.3  # Default for paper IDs without abstracts
        })

    return entries


def fetch_with_websearch() -> List[Dict]:
    """
    Fallback method: simulate web search results.
    In production, this would use actual WebSearch API.
    For now, returns empty list to indicate unavailability.
    """
    logger.info("WebSearch API not configured; skipping web search results")
    return []


def append_to_knowledge_brain(entries: List[Dict]) -> int:
    """
    Append scored and deduplicated entries to SECOND-KNOWLEDGE-BRAIN.md.
    Returns the number of entries added.
    """
    if not os.path.exists(BRAIN):
        logger.error(f"Knowledge brain not found: {BRAIN}")
        return 0

    # Read existing content
    with open(BRAIN, 'r', encoding='utf-8') as f:
        existing_content = f.read()

    # Extract existing hashes for deduplication
    existing_hashes = extract_existing_hashes(existing_content)
    logger.info(f"Found {len(existing_hashes)} existing entries in knowledge brain")

    # Score and filter entries
    scored_entries = []
    for entry in entries:
        entry_hash = hash_url(entry.get("url", ""))

        # Skip if already exists
        if entry_hash in existing_hashes:
            logger.debug(f"Skipping duplicate: {entry.get('title', 'Unknown')}")
            continue

        # Calculate or use existing relevance score
        if "relevance" not in entry:
            relevance = calculate_relevance_score(
                entry.get("title", ""),
                entry.get("abstract", "")
            )
        else:
            relevance = entry["relevance"]

        # Filter low-relevance entries
        if relevance <= 0:
            logger.debug(f"Skipping low-relevance entry: {entry.get('title', 'Unknown')}")
            continue

        entry["relevance"] = relevance
        entry["hash"] = entry_hash
        scored_entries.append(entry)

    # Sort by relevance (highest first)
    scored_entries.sort(key=lambda e: e["relevance"], reverse=True)

    # Prepare new entries
    if not scored_entries:
        logger.info("No new entries to add")
        return 0

    # Format entries for markdown
    today = datetime.date.today().isoformat()
    lines = [f"\n### Auto-crawl {today}\n"]

    for entry in scored_entries:
        url = entry.get("url", "N/A")
        venue = entry.get("venue", "Unknown")
        year = entry.get("year", str(datetime.date.today().year))
        title = entry.get("title", "Untitled")
        relevance = entry.get("relevance", 0)
        entry_hash = entry.get("hash", "")

        line = (f"- {today} — **{title}** ({venue}, {year}) "
                f"[{url}] relevance={relevance:.2f} <!--hash:{entry_hash}-->")
        lines.append(line)

    # Append to file
    try:
        with open(BRAIN, 'a', encoding='utf-8') as f:
            f.write("\n".join(lines) + "\n")

        logger.info(f"Successfully appended {len(scored_entries)} new entries")
        return len(scored_entries)

    except Exception as e:
        logger.error(f"Failed to append entries: {e}")
        return 0


def main():
    """Main execution flow."""
    logger.info("=" * 60)
    logger.info("knowledge_updater for skill #140 (smart-contract-code-security-audit)")
    logger.info("=" * 60)

    # Ensure directories exist
    ensure_directories()

    # Load state
    state = load_state()
    state["run_count"] += 1
    logger.info(f"Run #{state['run_count']} - Last run: {state.get('last_run', 'Never')}")

    # Fetch entries using available methods
    all_entries = []

    # Try crawl4ai first
    logger.info("Attempting to fetch with crawl4ai...")
    crawl4ai_entries = fetch_with_crawl4ai()
    all_entries.extend(crawl4ai_entries)

    # Try WebSearch as fallback
    if not all_entries:
        logger.info("Attempting to fetch with WebSearch...")
        websearch_entries = fetch_with_websearch()
        all_entries.extend(websearch_entries)

    # Append entries
    if all_entries:
        logger.info(f"Processing {len(all_entries)} total entries...")
        added = append_to_knowledge_brain(all_entries)

        # Update state
        state["last_run"] = datetime.datetime.now().isoformat()
        state["processed_urls"].extend([e.get("url", "") for e in all_entries])
        save_state(state)

        logger.info(f"Run complete: {added} new entries added to knowledge brain")

        if added == 0:
            logger.info("No new entries this run (all duplicates or low relevance)")
    else:
        logger.warning("No entries fetched - skill will operate in degraded mode")
        logger.info("Degraded mode: skill will use existing knowledge base")

    logger.info("=" * 60)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
