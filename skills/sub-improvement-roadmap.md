---
name: smart-contract-code-security-audit-sub-improvement-roadmap
description: Improvement Roadmap sub-skill for the Security Audit for Smart Contracts / Source Code (zero-day) harness — Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.
---

## Role
You are the **Improvement Roadmap** stage of the `smart-contract-code-security-audit` harness.

## Purpose
Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.

## Inputs
- Case context and outputs from the previous harness stage.

## Process
1. Take the upstream context.
2. Execute this stage's specific function (see below).
3. Validate against this stage's quality gate.
4. Return a structured result for the next stage.

## Roadmap Format
| Priority | Recommendation | Linked finding | Effort | Impact |
|---|---|---|
Order by impact-to-effort ratio; every item must trace to a scored finding.

## Prioritization Framework

### Impact Levels

**Critical (Impact: 9-10):**
- Direct fund loss possible
- Unauthorized access to sensitive functions
- Complete system compromise
- Regulatory compliance failure
- Examples: Reentrancy, access control bypass, private key exposure

**High (Impact: 7-8):**
- Significant operational disruption
- Data exposure or manipulation
- Partial fund loss possible
- Reputational damage
- Examples: Integer overflow in critical paths, DoS vulnerabilities

**Medium (Impact: 5-6):**
- Limited operational impact
- Minor data exposure
- Requires specific conditions to exploit
- Localized effects
- Examples: Gas optimization issues, minor validation gaps

**Low (Impact: 1-4):**
- Minimal operational impact
- Informational findings
- No direct security consequences
- Best practice recommendations
- Examples: Code style, documentation, non-critical optimizations

### Effort Levels

**Low (1-2 days):**
- Simple function-level changes
- Adding modifiers or checks
- Configuration updates
- Examples: Add onlyOwner modifier, implement reentrancy guard

**Medium (3-7 days):**
- Refactoring multiple functions
- Integration of security libraries
- Testing and verification
- Examples: Implement full access control system, add comprehensive validation

**High (2-4 weeks):**
- Architectural changes
- Major refactoring
- External dependencies
- Examples: Redesign state management, implement proxy pattern

**Very High (1-3 months):**
- Complete redesign
- Breaking changes
- External integrations
- Examples: Migrate to new platform, implement formal verification

### Priority Matrix

```
| Impact \ Effort | Low | Medium | High | Very High |
|----------------|-----|--------|------|------------|
| Critical       | P1  | P1     | P2   | P2         |
| High           | P1  | P2     | P3   | P3         |
| Medium         | P2  | P3     | P4   | P4         |
| Low            | P3  | P4     | SKIP | SKIP       |
```

**Priority Definitions:**
- **P1:** Fix immediately; critical risk, low/medium effort
- **P2:** Fix soon; high/critical risk with acceptable effort
- **P3:** Consider fixing; moderate risk, reasonable effort
- **P4:** Optional; low risk or high effort
- **SKIP:** Not recommended; low value, high cost

## Roadmap Item Template

```markdown
### Priority: [P1/P2/P3/P4]

**Recommendation:** [Concise, actionable fix statement]

**Linked Finding:** [Finding ID/Title from scoring phase]

**Effort Estimate:** [Low/Medium/High/Very High] — [X days/weeks]
- Reasoning: [why this effort level]

**Impact Level:** [Critical/High/Medium/Low]
- Consequence if not fixed: [what happens]

**Remediation Steps:**
1. [Specific step 1]
2. [Specific step 2]
3. [Specific step 3]

**Verification:**
- [ ] Test case: [describe test]
- [ ] Manual verification: [how to confirm]
- [ ] Tool verification: [Slither, Mythril, etc.]

**Resources:**
- [Framework reference]: [SWC/CWE/OWASP link]
- [Best practice guide]: [authoritative source]
```

## Complete Roadmap Example

```markdown
## Improvement Roadmap

### Priority: P1 (Critical - Fix Immediately)

**Recommendation:** Fix reentrancy vulnerability in withdraw() function

**Linked Finding:** Critical Vulnerabilities #1 - SWC-107

**Effort Estimate:** Low (1 day)
- Reasoning: Simple refactor to apply checks-effects-interactions pattern; no architectural changes needed

**Impact Level:** Critical
- Consequence if not fixed: Attacker can drain all protocol funds; complete loss of user deposits

**Remediation Steps:**
1. Move state update before external call
2. Add ReentrancyGuard modifier
3. Test with foundry/hardhat reentrancy scenarios

**Code Example:**
```solidity
// Before:
function withdraw(uint amount) public {
    (bool sent, ) = msg.sender.call{value: amount}("");
    require(sent, "Failed to send Ether");
    balances[msg.sender] -= amount;
}

// After:
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

function withdraw(uint amount) public nonReentrant {
    require(balances[msg.sender] >= amount, "Insufficient balance");
    balances[msg.sender] -= amount;
    (bool sent, ) = msg.sender.call{value: amount}("");
    require(sent, "Failed to send Ether");
}
```

**Verification:**
- [ ] Foundry reentrancy test passes
- [ ] Slither no reentrancy warnings
- [ ] Manual review confirms state before call

**Resources:**
- SWC-107: https://swcregistry.io/docs/SWC-107
- OpenZeppelin ReentrancyGuard: https://docs.openzeppelin.com/contracts/4.x/api/security

---

### Priority: P1 (High - Fix Immediately)

**Recommendation:** Implement access control on setFee() function

**Linked Finding:** Critical Vulnerabilities #2 - SWC-105

**Effort Estimate:** Low (0.5 day)
- Reasoning: Add onlyOwner modifier; straightforward access control implementation

**Impact Level:** Critical
- Consequence if not fixed: Anyone can modify protocol fees; economic attack vector

**Remediation Steps:**
1. Import Ownable from OpenZeppelin
2. Add onlyOwner modifier to setFee()
3. Test ownership transfer and access restrictions

**Code Example:**
```solidity
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityPool is Ownable {
    function setFee(uint256 newFee) public onlyOwner {
        require(newFee <= 1000, "Fee too high");
        fee = newFee;
    }
}
```

**Verification:**
- [ ] Test unauthorized call reverts
- [ ] Test owner can set fee
- [ ] Test ownership transfer works

**Resources:**
- SWC-105: https://swcregistry.io/docs/SWC-105
- OpenZeppelin Access Control: https://docs.openzeppelin.com/contracts/4.x/api/access

---

### Priority: P2 (Medium - Fix Soon)

**Recommendation:** Pin all dependency versions

**Linked Finding:** Dependency & Supply Chain - Unpinned dependencies

**Effort Estimate:** Low (1 day)
- Reasoning: Update package.json with locked versions; no code changes

**Impact Level:** Medium
- Consequence if not fixed: Potential supply chain compromise; unpredictable builds

**Remediation Steps:**
1. Audit current dependency versions
2. Update package.json with exact versions
3. Run npm audit
4. Commit lock files (package-lock.json)

**Verification:**
- [ ] npm install produces consistent results
- [ ] npm audit shows no vulnerabilities
- [ ] CI/CD builds are deterministic

**Resources:**
- npm audit: https://docs.npmjs.com/cli/v9/commands/npm-audit
- OWASP Dependency Check: https://owasp.org/www-project-dependency-check

---

### Priority: P3 (Low - Consider Fixing)

**Recommendation:** Implement comprehensive input validation

**Linked Finding:** Weakness Coverage - Missing validation patterns

**Effort Estimate:** Medium (1 week)
- Reasoning: Requires identifying all input points, implementing validation, extensive testing

**Impact Level:** Medium
- Consequence if not fixed: Potential edge case exploits; unexpected behavior

**Remediation Steps:**
1. Identify all external input points
2. Design validation library
3. Implement validation for each input
4. Add unit tests for validation logic

**Code Example:**
```solidity
library Validation {
    function validateAmount(uint256 amount) internal pure {
        require(amount > 0, "Amount must be positive");
        require(amount <= MAX_AMOUNT, "Amount exceeds maximum");
    }

    function validateAddress(address addr) internal pure {
        require(addr != address(0), "Invalid address");
    }
}
```

**Verification:**
- [ ] All external inputs validated
- [ ] Unit tests cover edge cases
- [ ] Manual review confirms completeness

**Resources:**
- SWC-102: https://swcregistry.io/docs/SWC-102
- Solidity Best Practices: https://consensys.github.io/smart-contract-best-practices

---

### Priority: P4 (Optional - Nice to Have)

**Recommendation:** Improve gas efficiency with batch operations

**Linked Finding:** Remediation Quality - Gas optimization suggestions

**Effort Estimate:** Medium (1 week)
- Reasoning: Requires refactoring to batch operations; significant testing

**Impact Level:** Low
- Consequence if not fixed: Higher gas costs; no security impact

**Remediation Steps:**
1. Identify batch operation opportunities
2. Design batch interface
3. Implement batch logic
4. Benchmark gas savings

**Verification:**
- [ ] Gas benchmarks show improvement
- [ ] Batch operations work correctly
- [ ] No functionality regression

**Resources:**
- Gas Optimization: https://docs.soliditylang.org/en/v0.8.17/techniques/optimizing-gas-consumption
```

## Traceability Matrix

Every roadmap item must trace back to a specific finding from the scoring phase:

| Roadmap Priority | Recommendation Source | Finding ID | Score Impact |
|------------------|----------------------|-----------|--------------|
| P1 | Critical Vulnerabilities | #1 | If unfixed: -15 points |
| P1 | Critical Vulnerabilities | #2 | If unfixed: -12 points |
| P2 | Dependencies | Unpinned | If unfixed: -5 points |
| P3 | Weakness Coverage | Validation | If unfixed: -8 points |
| P4 | Remediation Quality | Gas | If unfixed: -3 points |

## Implementation Timeline

**Immediate (0-2 weeks):**
- All P1 items
- Critical and high-risk findings

**Short-term (1-2 months):**
- P2 items
- Medium-risk findings with reasonable effort

**Medium-term (3-6 months):**
- P3 items
- Lower-risk improvements

**Long-term (6+ months):**
- P4 items
- Nice-to-have optimizations

## Output
A structured result the parent harness (`main.md`) consumes in the next stage.

## Quality Gate
- Output is complete, internally consistent, and (where it asserts facts) evidence-cited or framework-grounded before control returns to the harness.
- Every item traces to a scored finding
- Priority follows impact-to-effort ratio
- Remediation steps are actionable
- Verification methods are specified
- Effort estimates are justified
- Resource links are authoritative
