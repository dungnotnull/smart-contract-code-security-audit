# Test Scenarios — Security Audit for Smart Contracts / Source Code (zero-day) (Skill #140)

These scenarios validate the harness end-to-end: stage order, framework grounding, scoring with citations, gates, roadmap, and graceful degradation. Minimum 5 scenarios.

### Scenario 1: Reentrancy
- **User input:** "Audit this withdraw() function"
- **Expected behavior:** Skill threat-models, finds reentrancy/check-effects-interaction violation, CVSS, fix with guard.
- **Pass criteria:** correct stage order; framework named; scores cited; roadmap prioritized; limitations stated.
### Scenario 2: Access control
- **User input:** "Who can call this admin function?"
- **Expected behavior:** Skill maps access control, flags missing modifiers/ownership, severity, remediation.
- **Pass criteria:** correct stage order; framework named; scores cited; roadmap prioritized; limitations stated.
### Scenario 3: Dependency risk
- **User input:** "Is my package.json safe?"
- **Expected behavior:** Skill flags known-vuln dependencies/licenses, suggests pinned safe versions.
- **Pass criteria:** correct stage order; framework named; scores cited; roadmap prioritized; limitations stated.
### Scenario 4: Authorization context
- **User input:** "This is for our internal pentest of our own contract"
- **Expected behavior:** Skill proceeds with defensive audit framing, documents scope/authorization.
- **Pass criteria:** correct stage order; framework named; scores cited; roadmap prioritized; limitations stated.
### Scenario 5: Degraded mode
- **User input:** "Audit offline"
- **Expected behavior:** Falls back to SECOND-KNOWLEDGE-BRAIN, signals it can't fetch latest CVE/zero-day feeds.
- **Pass criteria:** correct stage order; framework named; scores cited; roadmap prioritized; limitations stated.

## Regression Notes
- Add real user runs here as regression cases.
- Verify `tools/knowledge_updater.py` dry-run appends well-formed entries and dedups by URL/DOI hash.
