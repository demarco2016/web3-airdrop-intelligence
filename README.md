# Web3 Airdrop Intelligence

Python application that monitors publicly available official Web3 announcements.

**Important**: This tool tracks public information only. It does not claim or guarantee any airdrop eligibility or rewards.

## Features

- Official announcement tracking (extendable sources)
- Snapshot and claim deadline tracking
- Project credibility indicators (official vs community)
- Duplicate detection
- Structured JSON output
- Configurable for GitHub Actions monitoring

## Installation

```bash
git clone https://github.com/demarco2016/web3-airdrop-intelligence.git
cd web3-airdrop-intelligence
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Usage

```bash
python monitor.py
```

Output is written to `output/report.json`.

## GitHub Actions

Add a workflow to run periodically and commit updated reports if desired.

## Disclaimer

Information is gathered from public sources. Always verify on official project channels. No airdrop is guaranteed.
