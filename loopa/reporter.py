"""
reporter.py

Generates and saves test reports for loopa load testing tool.
"""

import json

class Reporter:
    def __init__(self, filename="report.json"):
        self.filename = filename

    def save(self, metrics):
        with open(self.filename, "w") as f:
            json.dump(metrics, f, indent=2)

    def load(self):
        with open(self.filename, "r") as f:
            return json.load(f)
