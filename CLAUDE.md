# CLAUDE.md — Security Audit for Smart Contracts / Source Code (zero-day) (Skill #140)

**Cluster:** software-devops — A collection of skills for software development and operations tasks.

**Related Skills in Cluster:**
- Security review and code analysis skills
- Testing and validation skills
- Development workflow skills
- CI/CD and deployment skills

**Slug:** `smart-contract-code-security-audit`  •  **Cluster:** `software-devops`  •  **Source idea:** 140  •  **Phase:** Built (v1)

## Tagline
Audits smart contracts and source code for vulnerabilities, mapping findings to SWC/CWE/OWASP with severity and remediation.

## Problem This Skill Solves
Smart contracts and application code ship with reentrancy, access-control, and dependency vulnerabilities that lead to catastrophic exploits. This skill provides a systematic, standards-mapped security audit.

## Harness Flow Summary
1. **Intake** (`sub-intake`) — gather structured inputs, scope, goals.
2. **Framework selection** (`sub-framework-selector`) — choose named world-renowned framework(s).
3. **Research** (WebSearch/WebFetch + SECOND-KNOWLEDGE-BRAIN) — gather highest-tier evidence.
4. **Scoring** (`sub-scoring-engine`) — multi-dimensional weighted scores with citations.
5. **Challenge** — devil's-advocate review of assumptions and weak evidence.
6. **Roadmap** (`sub-improvement-roadmap`) — prioritized effort/impact recommendations.
7. **Synthesize** — assemble the professional deliverable; pass Quality Gates.

## Gates
- No mandatory safety/compliance gate for this cluster, but the standard Quality Gates below still apply.

## Sub-skills
- `skills/sub-intake.md` — Intake & Context Gathering: Collect the structured inputs, scope, and goals needed to run the analysis; ask clarifying questions when key facts are missing.
- `skills/sub-framework-selector.md` — Evaluation Framework Selector: Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
- `skills/sub-scoring-engine.md` — Scoring Engine: Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
- `skills/sub-improvement-roadmap.md` — Improvement Roadmap: Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.

## Tools Required
- `WebSearch`, `WebFetch` — live evidence and standards updates
- `Read`, `Write` — load knowledge base, emit deliverables
- `Bash` — run `tools/knowledge_updater.py`
- Skill tool — invoke sub-skills in sequence

## Knowledge Sources
- ArXiv: cs.CR
- Authoritative domain sources:
  - https://swcregistry.io
  - https://owasp.org
  - https://cwe.mitre.org
  - https://consensys.io/diligence
- Crawl queries: smart contract vulnerability reentrancy 2026; zero day disclosure CVE; defi exploit post-mortem; static analysis fuzzing solidity

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that grows `SECOND-KNOWLEDGE-BRAIN.md` (weekly cron recommended).

## Active Development Tasks
- [x] Scaffold full deliverable set
- [x] Define 4 sub-skills
- [ ] Expand SECOND-KNOWLEDGE-BRAIN with first live crawl
- [ ] Add regression cases from real user runs

## Related Root Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — self-improving knowledge base

---

## Cross-Skill Integration

### Sub-Skills Reusability
The following sub-skills are designed for reuse by sibling skills in the software-devops cluster:

1. **sub-intake** (Intake & Context Gathering)
   - Reusable for any analysis or review skill
   - Standardized intake questions and validation
   - Can be adapted for domain-specific contexts

2. **sub-framework-selector** (Evaluation Framework Selector)
   - Applicable to any evaluation-based skill
   - Framework selection logic is domain-agnostic
   - Modify candidate frameworks for different domains

3. **sub-scoring-engine** (Scoring Engine)
   - Generic multi-dimensional scoring rubric
   - Weighted scoring methodology transfers across domains
   - Adapt dimensions and weights for specific needs

4. **sub-improvement-roadmap** (Improvement Roadmap)
   - Universal prioritization framework
   - Effort/impact matrix applies broadly
   - Traceability requirements are domain-agnostic

### Integration Points
To integrate with this skill or use its sub-skills:

1. **For Security Analysis:**
   - Invoke the main harness for comprehensive audits
   - Use individual sub-skills for specific stages
   - Map domain-specific findings to SWC/CWE where applicable

2. **For Other Evaluations:**
   - Adapt sub-intake questions for your domain
   - Replace framework candidates in sub-framework-selector
   - Modify scoring dimensions in sub-scoring-engine
   - Adjust roadmap priorities in sub-improvement-roadmap

3. **Knowledge Base Sharing:**
   - SECOND-KNOWLEDGE-BRAIN.md can be extended
   - knowledge_updater.py pattern is reusable
   - Evidence hierarchy applies to any research-first skill

### Cluster Composition Standards
When contributing to the software-devops cluster:

1. Follow the sub-skill structure demonstrated here
2. Ensure clear input/output contracts between stages
3. Implement quality gates at each stage
4. Document framework choices with justification
5. Provide graceful degradation for offline operation
