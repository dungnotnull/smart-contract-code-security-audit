# PROJECT-detail.md — Security Audit for Smart Contracts / Source Code (zero-day) (Skill #140)

## Executive Summary
Audits smart contracts and source code for vulnerabilities, mapping findings to SWC/CWE/OWASP with severity and remediation. This skill is a full Claude harness in the **software-devops** cluster. It runs a research-first, framework-grounded workflow that scores the subject against named world-renowned methodologies and returns a prioritized improvement roadmap, while continuously updating its knowledge base.

## Problem Statement
Smart contracts and application code ship with reentrancy, access-control, and dependency vulnerabilities that lead to catastrophic exploits. This skill provides a systematic, standards-mapped security audit.

## Target Users & Use Cases
Practitioners, reviewers, and decision-makers who need an expert-grade, evidence-based assessment in this domain. Trigger examples:
1. **Reentrancy** — User: "Audit this withdraw() function" → Skill threat-models, finds reentrancy/check-effects-interaction violation, CVSS, fix with guard.
2. **Access control** — User: "Who can call this admin function?" → Skill maps access control, flags missing modifiers/ownership, severity, remediation.
3. **Dependency risk** — User: "Is my package.json safe?" → Skill flags known-vuln dependencies/licenses, suggests pinned safe versions.
4. **Authorization context** — User: "This is for our internal pentest of our own contract" → Skill proceeds with defensive audit framing, documents scope/authorization.
5. **Degraded mode** — User: "Audit offline" → Falls back to SECOND-KNOWLEDGE-BRAIN, signals it can't fetch latest CVE/zero-day feeds.

## Harness Architecture
```
/smart-contract-code-security-audit (main.md)
   ├── sub-intake .................... gather inputs & scope
   ├── sub-framework-selector ........ choose world-renowned framework(s)
   ├── [research] WebSearch/WebFetch + SECOND-KNOWLEDGE-BRAIN
   ├── sub-scoring-engine ............ multi-dimensional weighted scoring
   ├── [challenge] devil's-advocate assumption review
   ├── sub-improvement-roadmap ....... prioritized effort/impact actions
   └── synthesize ................... professional deliverable + quality gates
```

## Full Sub-Skill Catalog
### sub-intake — Intake & Context Gathering
- **Purpose:** Collect the structured inputs, scope, and goals needed to run the analysis; ask clarifying questions when key facts are missing.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.

### sub-framework-selector — Evaluation Framework Selector
- **Purpose:** Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.

### sub-scoring-engine — Scoring Engine
- **Purpose:** Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.

### sub-improvement-roadmap — Improvement Roadmap
- **Purpose:** Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.


## Evaluation Frameworks (World-Renowned, Citable)
| Framework / Standard | Role in this skill |
|---|---|
| SWC Registry & SCSVS | Smart Contract Weakness Classification and verification standard. |
| OWASP Top 10 / ASVS | Web application risks and verification standard. |
| CWE & CVSS v4 | Common Weakness Enumeration and severity scoring. |
| SANS/CWE Top 25 | Most dangerous software weaknesses. |
| Threat modeling (STRIDE) | Systematic threat enumeration. |

## Scoring Model
| Dimension | Weight | What is assessed |
|---|---|---|
| Critical vulnerabilities | 30% | reentrancy, access control, fund loss paths |
| Weakness coverage (SWC/CWE) | 20% | breadth of checks vs registries |
| Severity & exploitability (CVSS) | 20% | impact x likelihood scoring |
| Dependency & supply chain | 15% | vulnerable libs, license, pinning |
| Remediation quality | 15% | actionable, verified fixes |
Each dimension is scored 0-100 with cited evidence; the weighted total yields an overall grade (A: 90+, B: 75-89, C: 60-74, D: <60).

## Skill File Format Specification
- Frontmatter: `name`, `description`.
- Required sections: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates.

## E2E Execution Flow
1. Parse user request; if inputs are insufficient, `sub-intake` asks targeted questions.
2. `sub-framework-selector` picks framework(s) and justifies the choice.
3. Research stage gathers highest-tier evidence (see evidence hierarchy); degrade gracefully to SECOND-KNOWLEDGE-BRAIN if offline.
4. `sub-scoring-engine` scores each dimension with citations.
5. Challenge stage stress-tests conclusions.
6. `sub-improvement-roadmap` produces ranked actions.
7. Synthesize deliverable; run Quality Gates; present.

**Error handling:** missing inputs → ask; conflicting evidence → present both and grade certainty; tool failure → fallback + explicit limitation notice.

## SECOND-KNOWLEDGE-BRAIN Integration
- Sources: https://swcregistry.io, https://owasp.org, https://cwe.mitre.org, https://consensys.io/diligence
- ArXiv categories: cs.CR
- Crawl queries: smart contract vulnerability reentrancy 2026; zero day disclosure CVE; defi exploit post-mortem; static analysis fuzzing solidity
- Append format: dated entries with Title, Authors, Year, Venue, DOI/URL, key finding, relevance.

## Supporting Tools Spec
`tools/knowledge_updater.py`: inputs = source list + queries; outputs = appended SECOND-KNOWLEDGE-BRAIN entries; schedule = weekly cron; dedup by URL/DOI hash.

## Quality Gates (must all pass before final output)
- Every score cites at least one source or the chosen framework.
- Challenge stage completed; key assumptions tested.
- Roadmap items are prioritized by effort and impact and traceable to findings.
- Limitations and evidence certainty are stated explicitly.

## Test Scenarios
1. **Reentrancy** — User: "Audit this withdraw() function" → Skill threat-models, finds reentrancy/check-effects-interaction violation, CVSS, fix with guard.
2. **Access control** — User: "Who can call this admin function?" → Skill maps access control, flags missing modifiers/ownership, severity, remediation.
3. **Dependency risk** — User: "Is my package.json safe?" → Skill flags known-vuln dependencies/licenses, suggests pinned safe versions.
4. **Authorization context** — User: "This is for our internal pentest of our own contract" → Skill proceeds with defensive audit framing, documents scope/authorization.
5. **Degraded mode** — User: "Audit offline" → Falls back to SECOND-KNOWLEDGE-BRAIN, signals it can't fetch latest CVE/zero-day feeds.

## Key Design Decisions
1. Framework-grounded scoring (no ad-hoc criteria).
2. Research-first with graceful degradation to the local knowledge brain.
3. Mandatory challenge stage to counter confirmation bias.
4. Standard quality gates enforced before delivery.
5. Self-improving knowledge base via weekly crawl.
