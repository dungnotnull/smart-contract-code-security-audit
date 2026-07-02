# Sample Audit Reports — Security Audit for Smart Contracts / Source Code (Skill #140)

This document provides example outputs from the smart contract security audit skill for various scenarios. These templates demonstrate the expected format, depth, and quality of audit reports.

## Example 1: Solidity Smart Contract Audit (Reentrancy Focus)

### Input
```
User: "Audit this DeFi liquidity pool contract for security issues. We're planning to deploy to Ethereum mainnet next week."
```

### Output

# Security Audit Report: DeFiLiquidityPool.sol

## Executive Summary
**Overall Grade:** C (67.5/100)
**Key Finding:** Critical reentrancy vulnerability in withdraw() function combined with missing access controls
**Risk Level:** Critical — Not recommended for mainnet deployment without remediation

## Context & Scope
- **Framework Applied:** SWC Registry + SCSVS (primary), CWE/CVSS v4 (secondary), STRIDE (threat modeling)
- **Assessment Date:** 2026-07-02
- **Authorization:** Authorized pre-deployment review for own contract
- **Platform:** Ethereum mainnet (planned)
- **Language:** Solidity ^0.8.0

## Dimension Scores

| Dimension | Score | Weight | Weighted | Key Evidence |
|-----------|-------|--------|----------|--------------|
| Critical Vulnerabilities | 55 | 30% | 16.5 | Reentrancy (SWC-107), Access Control (SWC-105) |
| Weakness Coverage (SWC/CWE) | 75 | 20% | 15.0 | Covers 7/10 SWC categories; gaps in visibility |
| Severity & Exploitability (CVSS) | 65 | 20% | 13.0 | 1 Critical (CVSS 9.1), 1 High (CVSS 7.8) |
| Dependency & Supply Chain | 90 | 15% | 13.5 | All deps pinned; 1 outdated package |
| Remediation Quality | 70 | 15% | 10.5 | Fixes provided; verification incomplete |
| **TOTAL** | **67.5** | **100%** | **67.5** | **Grade: C** |

---

## Detailed Findings

### Critical Vulnerabilities

#### 1. Reentrancy in withdraw() Function
- **Severity:** Critical (CVSS 9.1)
- **Framework Reference:** SWC-107, CWE-841
- **Location:** `DeFiLiquidityPool.sol:145-152`

**Description:**
The withdraw() function performs an external call to msg.sender before updating the user's balance state. This creates a classic reentrancy vulnerability where an attacker can recursively call withdraw() before their balance is decremented, draining the contract.

**Code:**
```solidity
function withdraw(uint256 amount) external {
    require(balances[msg.sender] >= amount, "Insufficient balance");
    (bool sent, ) = msg.sender.call{value: amount}("");  // VULNERABLE
    require(sent, "Failed to send Ether");
    balances[msg.sender] -= amount;  // State update AFTER call
    emit Withdrawal(msg.sender, amount);
}
```

**Exploit Scenario:**
1. Attacker deposits funds
2. Attacker calls withdraw() with large amount
3. In fallback function of malicious contract, calls withdraw() again
4. Since balance not yet updated, second call succeeds
5. Repeat until contract drained
6. Historical precedent: DAO hack ($60M loss)

**Impact:** Complete loss of user funds; contract bankruptcy

**Remediation:**
Apply checks-effects-interactions pattern:
```solidity
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

function withdraw(uint256 amount) external nonReentrant {
    require(balances[msg.sender] >= amount, "Insufficient balance");
    balances[msg.sender] -= amount;  // State update BEFORE call
    (bool sent, ) = msg.sender.call{value: amount}("");
    require(sent, "Failed to send Ether");
    emit Withdrawal(msg.sender, amount);
}
```

**Verification:**
- [ ] Implement ReentrancyGuard from OpenZeppelin
- [ ] Move balance update before external call
- [ ] Run Slither: should show no reentrancy warnings
- [ ] Test with foundry reentrancy fuzzing

---

#### 2. Missing Access Control on setFee()
- **Severity:** Critical (CVSS 7.8)
- **Framework Reference:** SWC-105, CWE-286, CWE-862
- **Location:** `DeFiLiquidityPool.sol:87-90`

**Description:**
The setFee() function lacks access control modifiers, allowing any user to modify protocol fees. This could enable economic attacks where malicious actors set fees to 100% or 0% to disrupt operations.

**Code:**
```solidity
function setFee(uint256 newFee) external {  // NO ACCESS CONTROL
    fee = newFee;
    emit FeeUpdated(newFee);
}
```

**Exploit Scenario:**
1. Attacker calls setFee(10000) setting fee to 100%
2. All swap transactions fail due to excessive fees
3. Protocol becomes unusable (DoS)
4. Alternatively, setFee(0) eliminates revenue

**Impact:** Economic denial of service; protocol disruption

**Remediation:**
Add ownership access control:
```solidity
import "@openzeppelin/contracts/access/Ownable.sol";

contract DeFiLiquidityPool is Ownable {
    // ...

    function setFee(uint256 newFee) external onlyOwner {
        require(newFee <= 1000, "Fee cannot exceed 10%");
        fee = newFee;
        emit FeeUpdated(newFee);
    }
}
```

**Verification:**
- [ ] Add Ownable inheritance
- [ ] Apply onlyOwner modifier
- [ ] Test unauthorized call reverts
- [ ] Test owner can set fee

---

### High Severity Findings

#### 3. Integer Overflow in calculateReward()
- **Severity:** High (CVSS 7.2)
- **Framework Reference:** SWC-101, CWE-190
- **Location:** `DeFiLiquidityPool.sol:234-237`

**Description:**
Despite Solidity 0.8+ built-in overflow checks, unchecked block allows potential overflow in reward calculation edge cases.

**Code:**
```solidity
function calculateReward(uint256 principal, uint256 rate) external pure returns (uint256) {
    unchecked {
        return principal * rate / 10000;  // Potential overflow
    }
}
```

**Impact:** Incorrect reward calculations; user fund loss

**Remediation:**
Remove unchecked block or add overflow guards

---

### Medium Severity Findings

#### 4. Unchecked Return Value (transfer)
- **Severity:** Medium (CVSS 5.3)
- **Framework Reference:** SWC-112, CWE-252
- **Location:** Multiple locations

**Description:** Some token.transfer() calls don't check return value, which could fail silently for non-compliant tokens.

**Remediation:** Check boolean return or use safeTransfer pattern

---

## Improvement Roadmap

### Priority: P1 (Critical - Fix Immediately)

**1. Fix Reentrancy in withdraw()**
- **Linked Finding:** Critical Vulnerabilities #1 (SWC-107)
- **Effort:** Low (1 day) — Simple refactor, well-known pattern
- **Impact:** Critical — Prevents fund drainage
- **Steps:** Apply ReentrancyGuard, reorder operations, test with foundry

**2. Add Access Control to setFee()**
- **Linked Finding:** Critical Vulnerabilities #2 (SWC-105)
- **Effort:** Low (0.5 day) — Add onlyOwner modifier
- **Impact:** Critical — Prevents economic DoS
- **Steps:** Import Ownable, apply modifier, test access restrictions

---

### Priority: P2 (High - Fix Soon)

**3. Address Integer Overflow**
- **Linked Finding:** High Severity #3 (SWC-101)
- **Effort:** Low (1 day) — Remove unchecked or add guards
- **Impact:** High — Prevents calculation errors
- **Steps:** Review unchecked usage, add validation

---

### Priority: P3 (Medium - Consider Fixing)

**4. Fix Unchecked Return Values**
- **Linked Finding:** Medium Severity #4 (SWC-112)
- **Effort:** Medium (2 days) — Multiple locations to fix
- **Impact:** Medium — Prevents silent failures
- **Steps:** Implement safeTransfer pattern throughout

---

### Priority: P4 (Optional)

**5. Update Outdated Dependency**
- **Linked Finding:** Dependencies & Supply Chain
- **Effort:** Low (0.5 day) — Version bump
- **Impact:** Low — No known CVEs but best practice
- **Steps:** Update mocha from 9.2.0 to 10.x

---

## Limitations & Certainty

**Evidence Quality:** HIGH
- Framework references are authoritative (SWC Registry official)
- Code patterns are well-documented vulnerabilities
- Historical precedents confirm exploit feasibility

**Known Limitations:**
- Audit assumes standard deployment patterns
- Oracle interactions not assessed in detail
- Gas optimization not evaluated
- Formal verification not performed

**Assumptions:**
- Contract will be deployed on Ethereum mainnet
- Standard ERC20 token interactions
- No complex upgrade mechanisms
- OpenZeppelin contracts used as dependencies

**What Could Change Conclusion:**
- If contract includes upgrade mechanisms, reentrancy risk increases
- If protocol uses custom oracles, additional attack vectors exist
- If deployment differs from reviewed code, findings may not apply

**Certainty Levels:**
- Reentrancy finding: HIGH CERTAINTY — clear vulnerability pattern
- Access control finding: HIGH CERTAINTY — explicit missing protection
- Overflow finding: MEDIUM CERTAINTY — depends on actual usage context

---

## Sources

### Framework References
1. SWC Registry — https://swcregistry.io/docs/SWC-107 (Reentrancy)
2. SWC Registry — https://swcregistry.io/docs/SWC-105 (Unprotected Function)
3. SWC Registry — https://swcregistry.io/docs/SWC-101 (Integer Overflow)
4. SWC Registry — https://swcregistry.io/docs/SWC-112 (Unchecked Return Value)
5. CWE-841 — https://cwe.mitre.org/data/definitions/841.html (Improper Enforcement of Behavioral Workflow)
6. CWE-286 — https://cwe.mitre.org/data/definitions/286.html (Incorrect Privilege Assignment)
7. CWE-190 — https://cwe.mitre.org/data/definitions/190.html (Integer Overflow)

### Best Practices
8. OpenZeppelin Security — https://docs.openzeppelin.com/contracts/4.x/api/security (ReentrancyGuard)
9. OpenZeppelin Access Control — https://docs.openzeppelin.com/contracts/4.x/api/access (Ownable)
10. Consensus Best Practices — https://consensys.github.io/smart-contract-best-practices

### Historical Precedents
11. DAO Hack (2016) — https://www.coindesk.com/markets/2016/06/17/hacker-steals-60-million-ethereum-hours-bypass
12. Parity Wallet Hack (2017) — https://www.coindesk.com/business/2017/11/08/280-million-hacked

### Tools Used
13. Slither Static Analyzer — https://github.com/crytic/slither
14. CVSS Calculator v4 — https://www.first.org/cvss/calculator/4.0

---

## Example 2: Web Application API Audit

### Input
```
User: "Review our REST API for security issues. It handles user authentication and payment processing."
```

### Output Summary

# Security Audit Report: PaymentAPI REST Service

## Executive Summary
**Overall Grade:** B (82/100)
**Key Finding:** Broken access control on admin endpoints; lack of rate limiting
**Risk Level:** High — Generally sound with critical issues to address

## Context & Scope
- **Framework Applied:** OWASP ASVS (primary), CWE Top 25 (secondary), CVSS v4
- **Assessment Date:** 2026-07-02
- **Authorization:** Authorized internal audit

## Dimension Scores

| Dimension | Score | Weight | Weighted | Key Evidence |
|-----------|-------|--------|----------|--------------|
| Critical Vulnerabilities | 85 | 30% | 25.5 | No critical issues |
| Weakness Coverage (CWE) | 80 | 20% | 16.0 | Covers 8/10 OWASP categories |
| Severity & Exploitability (CVSS) | 75 | 20% | 15.0 | 1 High, 2 Medium findings |
| Dependency & Supply Chain | 85 | 15% | 12.75 | Minor outdated packages |
| Remediation Quality | 80 | 15% | 12.0 | Clear fixes provided |
| **TOTAL** | **82** | **100%** | **82** | **Grade: B** |

## Key Findings

### High Severity
1. **Broken Access Control (OWASP A01, CWE-286)**
   - Location: `/api/admin/*` endpoints
   - Issue: Admin endpoints lack role-based checks
   - Impact: Unauthorized administrative access

### Medium Severity
2. **Missing Rate Limiting (OWASP A04)**
   - Location: Authentication endpoints
   - Issue: No rate limiting on login attempts
   - Impact: Brute force attacks possible

3. **Insufficient Logging (OWASP A09)**
   - Location: Critical operations
   - Issue: Audit trail incomplete
   - Impact: Incident investigation difficulties

---

## Example 3: Dependency Security Scan

### Input
```
User: "Check package.json for security vulnerabilities in our Node.js project"
```

### Output Summary

# Dependency Security Audit Report

## Executive Summary
**Overall Grade:** B (78/100)
**Key Finding:** 2 high-severity CVEs in transitive dependencies; unpinned versions
**Risk Level:** Medium — Address critical dependencies before production

## Context & Scope
- **Framework Applied:** CWE/CVE database, SANS Top 25
- **File Analyzed:** package.json
- **Dependencies Scanned:** 24 direct, 156 total

## Dimension Scores

| Dimension | Score | Weight | Weighted | Key Evidence |
|-----------|-------|--------|----------|--------------|
| Critical Vulnerabilities | 70 | 30% | 21.0 | 2 High CVEs |
| Weakness Coverage (CWE) | 85 | 20% | 17.0 | Good coverage |
| Severity & Exploitability (CVSS) | 75 | 20% | 15.0 | High CVSS scores |
| Dependency & Supply Chain | 60 | 15% | 9.0 | Unpinned, outdated |
| Remediation Quality | 85 | 15% | 12.75 | Clear fixes |
| **TOTAL** | **78** | **100%** | **78** | **Grade: B** |

## Vulnerable Dependencies

### High Severity
1. **lodash < 4.17.21**
   - CVE: CVE-2021-23337 (CVSS 7.5)
   - Issue: Prototype pollution via zipObjectDeep
   - Fix: Update to >= 4.17.21
   - Path: project → dep1 → lodash

2. **axios < 0.21.1**
   - CVE: CVE-2021-3749 (CVSS 6.1)
   - Issue: SSRF via unsanitized URLs
   - Fix: Update to >= 0.21.1
   - Path: project → dep2 → axios

### Unpinned Dependencies
- express: ^4.18.0 → Should be 4.18.2
- mongoose: ^6.0.0 → Should be 6.0.13

---

## Example 4: Degraded Mode (Offline)

### Input
```
User: "Audit this contract [I'm offline]"
```

### Output

# Security Audit Report: [ContractName]

## Executive Summary
**Overall Grade:** C (65/100)
**Key Finding:** Access control and input validation concerns
**Risk Level:** Medium — Analysis based on cached knowledge (2026-06-18)

## Context & Scope
- **Framework Applied:** SWC Registry, CWE/CVSS (cached)
- **Assessment Date:** 2026-07-02
- **⚠️ MODE:** DEGRADED — Offline operation, using cached knowledge base

### Degraded Mode Notice
> **Important:** This analysis was performed in degraded mode without access to:
> - Latest CVE database updates
> - Recent vulnerability disclosures
> - Current security advisories
>
> Findings related to time-sensitive vulnerabilities (CVEs, zero-day exploits) should be re-verified when connectivity is restored. The knowledge base was last updated on 2026-06-18.

## Analysis Results
[Rest of report continues with standard format, but adds time-sensitivity warnings]

---

## Report Quality Checklist

All reports generated by this skill include:

- [ ] Executive summary with grade and key findings
- [ ] Context and scope documentation
- [ ] Chosen frameworks with justification
- [ ] Detailed dimension scores with evidence citations
- [ ] Prioritized improvement roadmap
- [ ] Limitations and certainty statements
- [ ] Complete source citations
- [ ] Clear remediation steps
- [ ] Verification procedures
- [ ] Resource links for further research
