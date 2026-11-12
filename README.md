# Cyber Threat Intelligence (CTI) Gathering and Analysis (Week 4 - Task 3)

## Overview
This repository contains the deliverables for **Week 4 - Task 3** of the Cyber Security Internship. The project focuses on gathering real-world threat intelligence from Open-Source Intelligence (OSINT) feeds, enriching Indicators of Compromise (IoCs), mapping attacker behaviors to the MITRE ATT&CK framework, and generating an actionable Threat Intelligence Report.

## Repository Structure
* `docs/CTI_Report.md` - Detailed Cyber Threat Intelligence report with executive summary, analysis, and mitigation steps.
* `data/iocs.csv` - Raw and enriched Indicators of Compromise (IPs, Domains, File Hashes).
* `scripts/enrich_iocs.py` - Python script used to defang IoCs and format threat data.

## Tools & Sources Used
* **Threat Feeds:** AlienVault OTX, AbuseIPDB, MalwareBazaar, OpenPhish
* **Enrichment & Mapping:** VirusTotal, MITRE ATT&CK Framework
* **Automation:** Python 3
