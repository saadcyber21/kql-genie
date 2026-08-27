# 🛡️ KQL-Genie: MITRE ATT&CK to Sentinel Mapper

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0-brightgreen.svg)](#)
[![CI/CD Ready](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange.svg)](#)

> **A zero-dependency, deterministic CLI tool** that instantly generates production-ready Microsoft Sentinel KQL hunting queries mapped directly to MITRE ATT&CK techniques.

---

## ⚡ The Challenge
SOC analysts and detection engineers spend countless hours translating MITRE ATT&CK tactics into functional KQL queries. Generic online generators produce bloated, inefficient queries that fail to account for specific Sentinel table schemas (e.g., `SigninLogs`, `SecurityEvent`, `OfficeActivity`), leading to high false-positive rates and alert fatigue.

## 🚀 The Solution
**KQL-Genie** provides a curated, lightweight mapping engine. Instead of relying on external APIs or heavy frameworks, it uses a local, version-controlled JSON database to instantly output optimized, copy-paste-ready KQL queries tailored for Microsoft Sentinel.

---

## 🏗️ Architecture

```mermaid
graph TD
    A[User Input: --technique T1059] --> B(KQL-Genie CLI)
    B --> C{Load mitre_kql.json}
    C -->|Parse| D[Extract Technique Metadata]
    C -->|Extract| E[Retrieve Optimized KQL Template]
    D --> F[Format Terminal Output]
    E --> F
    F --> G[Display / Export to .kql]
    
    style B fill:#1a1a2e,stroke:#e94560,stroke-width:2px,color:#fff
    style C fill:#0f3460,stroke:#fff,stroke-width:1px,color:#fff
        your CI/CD pipeline.

🤝 Contributing
Want to add a new MITRE technique or optimize a KQL query? 

    Fork the repository.
    Add your technique to mitre_kql.json.
    Submit a Pull Request. The GitHub Actions workflow will automatically validate your JSON syntax and CLI execution.

📄 License
This project is licensed under the MIT License