#!/usr/bin/env python3
"""Basic tests for the airdrop intelligence monitor."""

import unittest
from monitor import detect_duplicates, generate_report, track_deadlines

class TestMonitor(unittest.TestCase):
    def test_detect_duplicates(self):
        items = [
            {"project": "A", "title": "One"},
            {"project": "A", "title": "One"},
            {"project": "B", "title": "Two"}
        ]
        unique = detect_duplicates(items)
        self.assertEqual(len(unique), 2)

    def test_generate_report_has_disclaimer(self):
        report = generate_report([])
        self.assertIn("disclaimer", report)
        self.assertIn("No airdrop is guaranteed", report["disclaimer"])

    def test_track_deadlines(self):
        items = [{"deadline": None}]
        result = track_deadlines(items)
        self.assertEqual(result[0]["deadline_status"], "none")

if __name__ == "__main__":
    unittest.main()
