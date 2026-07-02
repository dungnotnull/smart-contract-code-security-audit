# SECOND-KNOWLEDGE-BRAIN.md — Security Audit for Smart Contracts / Source Code (zero-day) (Skill #140)

> Self-improving domain knowledge base. Grown by `tools/knowledge_updater.py` (weekly cron). Newest evidence is preferred per the evidence hierarchy (Systematic Review > Meta-Analysis > RCT > Cohort > Expert Opinion > Blog).

## Core Concepts & Frameworks

### SWC Registry & SCSVS
- **Full Name:** Smart Contract Weakness Classification and Smart Contract Security Verification Standard
- **Maintainer:** Smart Contract Security Researchers
- **Purpose:** Comprehensive classification of smart contract vulnerabilities
- **Key Resources:**
  - Registry: https://swcregistry.io
  - SCSVS: https://github.com/SmartContractSecurity/SCSVS
- **Critical SWC IDs:**
  - SWC-101: Integer Overflow and Underflow
  - SWC-102: Unsigned Integer Overflow
  - SWC-105: Unprotected Function
  - SWC-106: Unprotected SELFDESTRUCT
  - SWC-107: Reentrancy
  - SWC-108: State Variable Default Visibility
  - SWC-109: Address Prediction
  - SWC-110: Constructor Arguments Extraction
  - SWC-111: Use of Deprecated Solidity Features
  - SWC-112: Return Value of Transfer Not Checked
  - SWC-113: External Call Forwarding to User-Supplied Address
  - SWC-114: Authorization through tx.origin
  - SWC-115: Authorization bypass through Flexible Signature Verification
  - SWC-116: Block values as a proxy for time
  - SWC-117: Signature Replay Protection
  - SWC-118: Incorrect Constructor Name
  - SWC-119: Shadowing State Variables
  - SWC-120: Weak Randomness
  - SWC-121: Locking to Older Blocks
  - SWC-122: Lack of Signature Verification
  - SWC-123: Requirement Violation
  - SWC-124: Write to Arbitrary Storage Location
  - SWC-125: Incorrect Inheritance Order
  - SWC-126: Protection Against Signature Replay Attacks is Insufficient
  - SWC-127: Broken Weak Randomness
  - SWC-128: Assert Instruction Abuse
  - SWC-129: Type Casts with Truncation
  - SWC-130: Read-Only Reentrancy
  - SWC-131: Presence of unused variables
  - SWC-132: Arbitrary Storage Write
  - SWC-133: Price Manipulation Vulnerability
  - SWC-134: Short Address Issue
  - SWC-135: Gas Limit and Gas Optimization Issues
  - SWC-136: Uninitialized Logic Contract

### OWASP Top 10 / ASVS
- **Full Name:** Open Web Application Security Project
- **Purpose:** Web application security standards and verification
- **Key Resources:**
  - OWASP Top 10: https://owasp.org/www-project-top-ten/
  - ASVS: https://owasp.org/www-project-application-security-verification-standard
- **Current Top 10 (2021):**
  1. Broken Access Control
  2. Cryptographic Failures
  3. Injection
  4. Insecure Design
  5. Security Misconfiguration
  6. Vulnerable and Outdated Components
  7. Identification and Authentication Failures
  8. Software and Data Integrity Failures
  9. Security Logging and Monitoring Failures
  10. Server-Side Request Forgery (SSRF)

### CWE & CVSS v4
- **Full Name:** Common Weakness Enumeration and Common Vulnerability Scoring System
- **Maintainer:** MITRE Corporation
- **Purpose:** Universal weakness taxonomy and severity scoring
- **Key Resources:**
  - CWE: https://cwe.mitre.org
  - CVSS v4: https://www.first.org/cvss/calculator/4.0
- **Critical CWEs for Smart Contracts:**
  - CWE-20: Improper Input Validation
  - CWE-190: Integer Overflow or Wraparound
  - CWE-269: Improper Privilege Management
  - CWE-352: Cross-Site Request Forgery (CSRF)
  - CWE-400: Uncontrolled Resource Consumption
  - CWE-502: Deserialization of Untrusted Data
  - CWE-787: Out-of-bounds Write
  - CWE-841: Improper Enforcement of Behavioral Workflow (similar to reentrancy)
  - CWE-862: Missing Authorization
  - CWE-863: Incorrect Authorization
  - CWE-1230: Improper Validation of Specified Integrity Check Value

### SANS/CWE Top 25
- **Purpose:** Most dangerous software weaknesses
- **Resource:** https://cwe.mitre.org/top25/archive/2023/2023_top25_list.html
- **Categories:** Injection, Buffer Overflow, Cryptographic Issues, Authorization

### Threat Modeling (STRIDE)
- **Acronym:** Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- **Purpose:** Systematic threat enumeration
- **Application:** Smart contract threat analysis, external interaction assessment

## Key Research Papers

### Smart Contract Security
| Title | Authors | Year | Venue | DOI/Link | Relevance |
|---|---|---|---|---|---|
| "SoK: Scanning Smart Contracts with Higher-Order Domain Specific Languages" | Sergey, et al. | 2023 | IEEE S&P | https://doi.org/10.1109/SP46214.2023.10179365 | Static analysis tools comparison |
| "Smart Contract Vulnerabilities: An Exhaustive Classification" | Salehi, et al. | 2021 | ArXiv | https://arxiv.org/abs/2105.08376 | Vulnerability taxonomy |
| "DeFi Safety Revisited" | He, et al. | 2022 | ACM CCS | https://doi.org/10.1145/3546917 | DeFi-specific vulnerabilities |
| "A Survey on Smart Contract Security: Issues, Vulnerabilities, and Defenses" | Chen, et al. | 2023 | ArXiv | https://arxiv.org/abs/2301.03378 | Comprehensive overview |
| "Reentrancy Attacks in Smart Contracts: A Comprehensive Study" | Kalstad, et al. | 2022 | ArXiv | https://arxiv.org/abs/2209.08302 | Reentrancy deep dive |

### Formal Verification
| Title | Authors | Year | Venue | DOI/Link | Relevance |
|---|---|---|---|---|---|
| "Certora: Formal Verification for Smart Contracts" | Certora Team | 2023 | Documentation | https://www.certora.com/docs | Formal verification methodology |
| "Verifying Smart Contracts with SMT Solvers" | Hildenbrandt, et al. | 2021 | IEEE S&P | https://doi.org/10.1109/SP40000.2021.00058 | SMT-based verification |

## State-of-the-Art Methods & Tools

### Static Analysis Tools
- **Slither** - Solidity static analyzer
  - Repository: https://github.com/crytic/slither
  - Output: Vulnerability detection, code visualization
  - Strengths: Fast, comprehensive checks, extensible

- **Mythril** - Symbolic execution analyzer
  - Repository: https://github.com/ConsenSys/mythril
  - Output: Execution path analysis, vulnerability detection
  - Strengths: Deep analysis, false positive reduction

- **Securify** - Security analyzer for smart contracts
  - Website: https://securify.ch
  - Output: Pattern-based vulnerability detection
  - Strengths: Compliance checking, pattern matching

- **Certora** - Formal verification platform
  - Website: https://www.certora.com
  - Output: Mathematical proof of correctness
  - Strengths: Highest assurance, complex property checking

### Dynamic Analysis Tools
- **Foundry** - Testing framework
  - Repository: https://github.com/foundry-rs/foundry
  - Output: Unit tests, fuzzing, property-based testing
  - Strengths: Fast execution, comprehensive testing

- **Echidna** - Property-based testing
  - Repository: https://github.com/crytic/echidna
  - Output: Fuzzing results, counterexamples
  - Strengths: Boundary case detection

- **Hardhat** - Development environment
  - Repository: https://github.com/NomicFoundation/hardhat
  - Output: Testing, deployment, debugging
  - Strengths: Integrated development workflow

## Authoritative Data Sources

### Smart Contract Vulnerability Databases
- **SWC Registry:** https://swcregistry.io
  - Comprehensive smart contract weakness classification
  - Maintained by security researchers
  - Maps to CWE for cross-referencing

- **Consensys Diligence:** https://consensys.io/diligence
  - Auditing firm with public vulnerability disclosures
  - Blog contains detailed post-mortems
  - Smart contract security best practices

- **Immunefi:** https://www.immunefi.com
  - Bug bounty platform for DeFi/Web3
  - Real-world vulnerability reports
  - Payout data for severity assessment

### General Security Databases
- **CVE Database:** https://cve.mitre.org
  - Universal vulnerability catalog
  - CVSS scores included
  - Cross-reference with CWE

- **NVD (National Vulnerability Database):** https://nvd.nist.gov
  - U.S. government vulnerability database
  - Detailed CVE information
  - CVSS calculator integration

- **CWE Database:** https://cwe.mitre.org
  - Comprehensive weakness taxonomy
  - Maps to multiple frameworks
  - Prevention and mitigation guidance

### Academic Sources
- **ArXiv cs.CR:** https://arxiv.org/list/cs.CR/recent
  - Cryptography and security papers
  - Latest research findings
  - Pre-publication access

- **Google Scholar:** Smart contract security queries
  - Academic literature search
  - Citation tracking
  - Authoritative sources

## Analytical Frameworks (Scoring Backbone)

| Framework / Standard | Role in this skill | Primary Focus |
|---|---|---|
| SWC Registry & SCSVS | Smart Contract Weakness Classification and verification standard | Smart contract-specific vulnerabilities |
| OWASP Top 10 / ASVS | Web application risks and verification standard | Traditional web security |
| CWE & CVSS v4 | Common Weakness Enumeration and severity scoring | Universal weakness taxonomy and scoring |
| SANS/CWE Top 25 | Most dangerous software weaknesses | High-priority weaknesses |
| Threat modeling (STRIDE) | Systematic threat enumeration | Threat identification and analysis |

## Evidence Hierarchy (for Research Stage)

1. **Primary Standards Documents** (Highest Trust)
   - SWC Registry official documentation
   - OWASP standards and guides
   - CWE/CVSS official specifications
   - Official protocol documentation

2. **Peer-Reviewed Academic Papers**
   - ArXiv cs.CR with subsequent publication
   - Major security conferences (IEEE S&P, ACM CCS, USENIX Security)
   - Journal articles with peer review

3. **Industry Best Practices**
   - Consensys Diligence guides
   - Reputable audit firm publications
   - OpenZeppelin documentation

4. **Vendor Documentation**
   - Tool documentation (Slither, Mythril, etc.)
   - Platform-specific guides
   - Framework documentation

5. **Blog Posts and Community Resources** (Lowest Trust)
   - Individual developer blogs
   - Community forums
   - Social media discussions
   - **Always verify against higher-tier sources**

## Self-Update Protocol (crawl4ai config)

### Sources
- ArXiv categories: cs.CR (Cryptography and Security), cs.SE (Software Engineering)
- Web sources: SWC Registry, OWASP, CWE, Consensys Diligence
- Search queries configured for domain relevance

### Search Queries
```
smart contract vulnerability reentrancy 2026
zero day disclosure CVE
defi exploit post-mortem
static analysis fuzzing solidity
smart contract security audit 2026
blockchain vulnerability detection
```

### Frequency
- **Recommended:** Weekly cron job
- **Minimum:** Monthly updates
- **On-demand:** Before major audits

### Append Format
```markdown
### Auto-crawl YYYY-MM-DD
- YYYY-MM-DD — **[Paper Title]** ([Venue], [Year]) [URL] relevance=X.XX <!--hash:XXXXXXXX-->
```

### Deduplication
- Uses SHA-256 hash of normalized URL
- Checks existing hashes in file
- Skips duplicates automatically

## Knowledge Update Log

### 2026-06-18
- Knowledge base seeded at skill creation
- Frameworks and sources documented
- Crawl infrastructure implemented
- First live crawl pending

### Auto-Crawl Entries
<!-- New entries will be appended here by knowledge_updater.py -->
