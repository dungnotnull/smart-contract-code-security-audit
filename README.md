# Security Audit for Smart Contracts / Source Code

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cluster: software-devops](https://img.shields.io/badge/Cluster-software--devops-green)](https://skills.smartcontract.dev)

A production-grade Claude Code skill that audits smart contracts and source code for vulnerabilities, mapping findings to SWC/CWE/OWASP standards with severity scoring and prioritized remediation.

## Overview

This skill provides systematic, framework-grounded security audits for:
- Smart contracts (Solidity, Rust, Vyper, etc.)
- Web applications and APIs
- Software supply chains and dependencies
- General source code security assessments

It operates research-first, grounding every judgment in world-renowned frameworks (SWC Registry, OWASP, CWE/CVSS) while continuously updating its knowledge base through automated web crawling.

## Features

- **Framework-Grounded Analysis**: Uses recognized security standards (SWC, OWASP, CWE/CVSS)
- **Multi-Dimensional Scoring**: Five weighted dimensions with evidence-backed scoring
- **Prioritized Roadmaps**: Effort/impact-ranked remediation recommendations
- **Graceful Degradation**: Works offline with cached knowledge when needed
- **Self-Improving**: Weekly knowledge updates via automated crawling
- **Production-Ready**: Comprehensive testing, quality gates, and documentation

## Installation

### Requirements
- Claude Code CLI (latest version)
- Python 3.8+ (for knowledge updater tool)
- Optional: crawl4ai library for live knowledge updates

### Setup

1. **Clone or download this skill directory:**
   ```bash
   git clone https://github.com/yourusername/smart-contract-code-security-audit.git
   cd smart-contract-code-security-audit
   ```

2. **Install optional dependencies (for knowledge updates):**
   ```bash
   pip install crawl4ai
   ```

3. **Verify installation:**
   ```bash
   ls skills/
   # Should show: main.md, sub-*.md files
   ```

## Usage

### Basic Usage

Trigger the skill by asking Claude Code to audit your code:

```
Audit this withdraw() function for security issues
```

```
Review this smart contract for reentrancy vulnerabilities
```

```
Check my package.json for security risks
```

### Advanced Usage

**Specify Framework:**
```
Audit this contract using SWC and CWE frameworks
```

**Focus Area:**
```
Analyze the access control mechanisms in this contract
```

**Scope Definition:**
```
Review only the external call functions for vulnerabilities
```

### Sample Workflow

1. **Intake**: Skill asks targeted questions if context is missing
2. **Framework Selection**: Chooses appropriate security standards
3. **Research**: Gathers latest evidence (or uses cached knowledge)
4. **Scoring**: Applies multi-dimensional rubric with citations
5. **Challenge**: Tests assumptions and grades certainty
6. **Roadmap**: Generates prioritized remediation plan
7. **Synthesis**: Produces professional audit report

## Documentation

### Core Documentation
- **[PROJECT-detail.md](PROJECT-detail.md)**: Full technical specification
- **[PROJECT-DEVELOPMENT-PHASE-TRACKING.md](PROJECT-DEVELOPMENT-PHASE-TRACKING.md)**: Development phase tracking
- **[CLAUDE.md](CLAUDE.md)**: Skill behavior guidelines
- **[SECOND-KNOWLEDGE-BRAIN.md](SECOND-KNOWLEDGE-BRAIN.md)**: Domain knowledge base

### Skill Structure
```
smart-contract-code-security-audit/
├── skills/
│   ├── main.md                    # Main harness
│   ├── sub-intake.md              # Intake & context gathering
│   ├── sub-framework-selector.md  # Framework selection
│   ├── sub-scoring-engine.md      # Scoring engine
│   └── sub-improvement-roadmap.md # Remediation roadmap
├── tools/
│   └── knowledge_updater.py       # Self-improving knowledge pipeline
├── tests/
│   └── test-scenarios.md          # Test scenarios
├── SECOND-KNOWLEDGE-BRAIN.md      # Domain knowledge base
├── PROJECT-detail.md              # Technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md
├── CLAUDE.md                       # Skill guidelines
└── README.md                      # This file
```

## Supported Frameworks

| Framework | Purpose | Coverage |
|---|---|---|
| SWC Registry | Smart contract weaknesses | Ethereum, Solana, general blockchain |
| OWASP/ASVS | Web application security | APIs, web apps, traditional software |
| CWE/CVSS v4 | Universal weakness taxonomy | All software types |
| SANS Top 25 | Most dangerous weaknesses | General software security |
| STRIDE | Threat modeling | Systematic threat analysis |

## Scoring Model

The skill evaluates code across five dimensions:

| Dimension | Weight | Assessment |
|---|---|---|
| Critical Vulnerabilities | 30% | Reentrancy, access control, fund loss |
| Weakness Coverage | 20% | SWC/CWE registry alignment |
| Severity & Exploitability | 20% | CVSS-based scoring |
| Dependencies & Supply Chain | 15% | Vulnerable libs, licensing |
| Remediation Quality | 15% | Actionable, verified fixes |

**Overall Grades:**
- A (90-100): Production-ready
- B (75-89): Generally sound
- C (60-74): Remediation required
- D (0-59): Not recommended

## Output Format

Each audit produces a structured report:

1. **Executive Summary**: Overall grade and headline findings
2. **Context & Scope**: Assessment parameters and chosen frameworks
3. **Dimension Scores**: Detailed scoring with cited evidence
4. **Findings & Risks**: Analysis with severity and exploitability
5. **Improvement Roadmap**: Prioritized, effort/impact-ranked actions
6. **Limitations & Certainty**: Evidence quality and assumptions
7. **Sources**: Full citation list

## Knowledge Updates

The skill maintains an up-to-date knowledge base through:

### Automated Updates
```bash
# Run manually
python tools/knowledge_updater.py

# Or set up weekly cron
0 2 * * 0 /usr/bin/python3 /path/to/tools/knowledge_updater.py
```

### Update Sources
- ArXiv cs.CR (latest security research)
- SWC Registry (smart contract vulnerabilities)
- OWASP (web security standards)
- CWE/CVE databases (known vulnerabilities)
- Consensys Diligence (best practices)

## Testing

Test scenarios are defined in [tests/test-scenarios.md](tests/test-scenarios.md):

1. **Reentrancy Detection**: Withdrawal function audit
2. **Access Control**: Admin function review
3. **Dependency Risk**: Package manifest analysis
4. **Authorization Context**: Internal pentest framing
5. **Degraded Mode**: Offline operation testing

## Contributing

We welcome contributions! Please:

1. Check existing issues for your concern
2. Fork the repository
3. Create a feature branch
4. Make your changes with tests
5. Submit a pull request

### Contribution Areas
- Additional framework mappings
- New vulnerability patterns
- Tool integrations
- Documentation improvements
- Test scenarios

## Quality Assurance

Before release, all code passes:

1. **Code Review**: Superpowers code-reviewer agent validation
2. **Tests Pass**: All test scenarios execute correctly
3. **Clean Startup**: No errors or warnings
4. **Documentation**: All changes tracked in development log

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Citation

If you use this skill in your work:

```
Security Audit for Smart Contracts / Source Code (Skill #140).
Cluster: software-devops. Version 1.0.0.
https://github.com/yourusername/smart-contract-code-security-audit
```

## Acknowledgments

Built with:
- **SWC Registry** for smart contract weakness classification
- **OWASP** for web security standards
- **MITRE/CWE** for vulnerability taxonomy
- **ConsenSys Diligence** for best practices
- The Claude Code community for skill framework

## Version History

- **v1.0.0** (2026-07-02): Initial production release
  - Complete harness implementation
  - All 5 sub-skills operational
  - Knowledge pipeline functional
  - Test scenarios validated
  - Documentation complete

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review test scenarios for examples

## Roadmap

Future enhancements planned:
- Additional language support (Vyper, Rust for Solana)
- More framework integrations
- Enhanced tool automation
- Real-time threat intelligence feeds
- Collaborative audit features

---

**Built with Claude Code** — https://claude.com/claude-code

*A production-ready skill for systematic security audits grounded in world-renowned frameworks.*
