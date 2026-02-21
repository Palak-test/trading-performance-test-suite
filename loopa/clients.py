"""
clients.py

Handles HTTP client logic for loopa load testing tool.
"""

import requests

class LoopaClient:
    def __init__(self, host):
        self.host = host

    def get(self, path):
        return requests.get(f"{self.host}{path}")

    def post(self, path, data=None):
        return requests.post(f"{self.host}{path}", data=data)
