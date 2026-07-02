---
name: smart-contract-code-security-audit-sub-framework-selector
description: Evaluation Framework Selector sub-skill for the Security Audit for Smart Contracts / Source Code (zero-day) harness — Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
---

## Role
You are the **Evaluation Framework Selector** stage of the `smart-contract-code-security-audit` harness.

## Purpose
Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.

## Inputs
- Case context and outputs from the previous harness stage.

## Process
1. Take the upstream context.
2. Execute this stage's specific function (see below).
3. Validate against this stage's quality gate.
4. Return a structured result for the next stage.

## Candidate Frameworks
| Framework / Standard | Role in this skill | Best For |
|---|---|---|
| SWC Registry & SCSVS | Smart Contract Weakness Classification and verification standard. | Blockchain smart contracts (EVM, Solana, etc.) |
| OWASP Top 10 / ASVS | Web application risks and verification standard. | Web apps, APIs, traditional software |
| CWE & CVSS v4 | Common Weakness Enumeration and severity scoring. | All software - universal weakness taxonomy |
| SANS/CWE Top 25 | Most dangerous software weaknesses. | General software security focus |
| Threat modeling (STRIDE) | Systematic threat enumeration. | System-level threat analysis |

## Selection Logic

### Decision Tree

```
┌─────────────────────────────────────────┐
│        START: What is the subject?      │
└─────────────────┬───────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
    ▼             ▼             ▼
Smart        Web App      Traditional
Contract     / API         Software
    │             │             │
    │             │             │
    ▼             ▼             ▼
┌─────────┐ ┌──────────┐ ┌──────────┐
│ PRIMARY │ │ PRIMARY  │ │ PRIMARY  │
│SWC+SCSVS│ │OWASP+ASVS│ │CWE Top 25│
└────┬────┘ └─────┬────┘ └─────┬────┘
     │            │            │
     └────────────┼────────────┘
                  │
                  ▼
         ┌────────────────┐
         │ SECONDARY ALL  │
         │CWE+CVSS v4     │
         │STRIDE (if sys) │
         └────────────────┘
```

### Framework Combinations

**Smart Contract Audit:**
- **Primary:** SWC Registry + SCSVS (Smart Contract Specific)
- **Secondary:** CWE/CVSS v4 (severity scoring), STRIDE (threat modeling)
- **Rationale:** SWC provides domain-specific weakness taxonomy; CWE/CVSS standardizes severity

**Web Application/API:**
- **Primary:** OWASP ASVS (verification standard)
- **Secondary:** CWE Top 25, CVSS v4 (scoring), STRIDE (threats)
- **Rationale:** OWASP is the industry standard for web security

**General Software Security:**
- **Primary:** CWE Top 25 + SANS
- **Secondary:** CVSS v4, STRIDE
- **Rationale:** CWE provides comprehensive weakness enumeration

**Supply Chain/Dependencies:**
- **Primary:** CWE (vulnerability taxonomy)
- **Secondary:** CVE database, SBOM analysis
- **Rationale:** CWE maps directly to CVE vulnerability reports

### Selection Guidelines

**Always Include CWE/CVSS:**
- CWE provides universal weakness enumeration
- CVSS v4 standardizes severity scoring
- Use these for ALL assessments as the baseline

**Add Domain-Specific Frameworks:**
- Smart contracts → SWC (non-negotiable)
- Web/apps → OWASP (industry standard)
- System design → STRIDE (threat modeling)

**Framework Co-Application:**
- Use multiple frameworks when beneficial
- Map findings across frameworks (e.g., SWC-107 ≈ CWE-841)
- Note overlaps and avoid double-counting in scores

### Justification Template

```markdown
## Selected Frameworks

**Primary Framework(s):** [framework names]

**Justification:**
For this [subject type], I'm applying [framework(s)] because [specific reason].

**Framework Relevance:**
- [Framework 1]: [what it covers, why it applies]
- [Framework 2]: [what it covers, why it applies]

**Supporting Standards:**
- [CWE/CVSS]: Universal weakness taxonomy and severity scoring
- [STRIDE if applicable]: Systematic threat enumeration

**Framework Source:**
- [Official documentation link]
- [Version/date of standard applied]
```

### Example Justifications

**Example 1: Solidity DeFi Contract**
```markdown
## Selected Frameworks

**Primary:** SWC Registry + SCSVS
**Secondary:** CWE/CVSS v4, STRIDE

**Justification:**
For this Solidity DeFi smart contract, I'm applying the SWC Registry and SCSVS because they provide the industry-standard taxonomy for smart contract weaknesses specific to Ethereum Virtual Machine (EVM) contracts. These frameworks cover critical issues like reentrancy (SWC-107), access control (SWC-105), and arithmetic issues (SWC-101) that are most prevalent in DeFi protocols.

**Framework Relevance:**
- SWC Registry: Domain-specific weakness classification for smart contracts
- SCSVS: Verification standard for smart contract security best practices
- CWE/CVSS v4: Universal weakness mapping and standardized severity scoring
- STRIDE: Threat modeling for external interactions and oracle dependencies

**Framework Source:**
- https://swcregistry.io (accessed 2026-07-02)
- CVSS v4 specification: https://www.first.org/cvss/calculator/4.0
```

**Example 2: Web Application API**
```markdown
## Selected Frameworks

**Primary:** OWASP ASVS
**Secondary:** CWE Top 25, CVSS v4

**Justification:**
For this REST API, I'm applying OWASP ASVS because it's the industry-standard verification standard for web application security. ASVS provides comprehensive coverage of authentication, authorization, input validation, and output encoding—areas where APIs most commonly fail.

**Framework Relevance:**
- OWASP ASVS: Systematic verification requirements for web applications
- CWE Top 25: Most dangerous software weaknesses (injection, broken auth, etc.)
- CVSS v4: Standardized severity scoring for identified vulnerabilities

**Framework Source:**
- https://owasp.org/www-project-application-security-verification-standard
```

**Example 3: Supply Chain Dependency Scan**
```markdown
## Selected Frameworks

**Primary:** CWE + CVE database
**Secondary:** SANS Top 25, CVSS v4

**Justification:**
For this dependency manifest analysis, I'm applying CWE and CVE databases because they provide the definitive mapping of known vulnerabilities in software components. This approach allows direct lookup of published vulnerabilities (CVEs) and their categorization (CWE) for each dependency.

**Framework Relevance:**
- CWE: Comprehensive weakness enumeration for all software types
- CVE Database: Known published vulnerabilities with severity scores
- SANS Top 25: Focus on most dangerous and common weaknesses
- CVSS v4: Standardized severity and exploitability scoring

**Framework Source:**
- https://cwe.mitre.org
- https://nvd.nist.gov/vuln/search
```

### Edge Cases

**Cross-Domain Subjects:**
If the subject spans domains (e.g., smart contract with web frontend):
1. Apply both primary frameworks
2. Clearly separate domain-specific findings
3. Note any shared concerns (e.g., authentication)

**No Clear Framework:**
If no framework perfectly matches:
1. Use CWE/CVSS as universal baseline
2. Supplement with closest relevant framework(s)
3. Explicitly state the limitation

**Framework Conflicts:**
If frameworks disagree:
1. Document the conflict
2. Explain both perspectives
3. Default to more conservative/protective interpretation

## Output
A structured result the parent harness (`main.md`) consumes in the next stage.

## Quality Gate
- Output is complete, internally consistent, and (where it asserts facts) evidence-cited or framework-grounded before control returns to the harness.
