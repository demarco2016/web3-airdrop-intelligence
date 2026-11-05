#!/usr/bin/env python3
"""
Web3 Airdrop Intelligence Monitor
Tracks publicly available official announcements.
Does not claim any airdrop is guaranteed.
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Configurable official sources (extend with real public feeds)
SOURCES = [
    {"name": "Example Project", "url": "https://example.com/announcements", "type": "official", "credibility": 90},
    {"name": "Community Source", "url": "https://example.com/community", "type": "community", "credibility": 50}
]

def fetch_announcements() -> List[Dict]:
    """Placeholder for fetching public announcements."""
    return [
        {
            "project": "Example",
            "title": "Sample Announcement",
            "url": "https://example.com",
            "deadline": (datetime.utcnow() + timedelta(days=14)).isoformat() + "Z",
            "credibility": 90,
            "source_type": "official",
            "notes": "Publicly available info only. Not a guarantee."
        },
        {
            "project": "Example",
            "title": "Sample Announcement",
            "url": "https://example.com",
            "deadline": None,
            "credibility": 50,
            "source_type": "community",
            "notes": "Duplicate test."
        }
    ]

def detect_duplicates(items: List[Dict]) -> List[Dict]:
    seen = set()
    unique = []
    for item in items:
        key = (item.get("project"), item.get("title"))
        if key not in seen:
            seen.add(key)
            unique.append(item)
    return unique

def track_deadlines(items: List[Dict]) -> List[Dict]:
    """Add deadline status."""
    now = datetime.utcnow()
    for item in items:
        dl = item.get("deadline")
        if dl:
            try:
                deadline_dt = datetime.fromisoformat(dl.replace("Z", ""))
                days_left = (deadline_dt - now).days
                item["days_until_deadline"] = max(0, days_left)
                item["deadline_status"] = "upcoming" if days_left > 0 else "passed"
            except Exception:
                item["deadline_status"] = "unknown"
        else:
            item["deadline_status"] = "none"
    return items

def score_credibility(items: List[Dict]) -> List[Dict]:
    """Enhance credibility indicators."""
    for item in items:
        base = item.get("credibility", 50)
        if item.get("source_type") == "official":
            item["credibility_score"] = min(100, base + 10)
        else:
            item["credibility_score"] = base
        item["credibility_label"] = "high" if item["credibility_score"] >= 80 else "medium" if item["credibility_score"] >= 60 else "low"
    return items

def generate_report(items: List[Dict]) -> Dict:
    processed = detect_duplicates(items)
    processed = track_deadlines(processed)
    processed = score_credibility(processed)
    return {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "disclaimer": "Information from public sources. No airdrop is guaranteed.",
        "total_unique": len(processed),
        "announcements": processed
    }

def main():
    announcements = fetch_announcements()
    report = generate_report(announcements)
    os.makedirs("output", exist_ok=True)
    with open("output/report.json", "w") as f:
        json.dump(report, f, indent=2)
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
