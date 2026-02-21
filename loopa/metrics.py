"""
metrics.py

Provides performance metrics collection for loopa load testing tool.
"""

import time

class Metrics:
    def __init__(self):
        self.start_time = time.time()
        self.requests = 0
        self.errors = 0
        self.response_times = []

    def record_request(self, response_time, error=False):
        self.requests += 1
        self.response_times.append(response_time)
        if error:
            self.errors += 1

    def summary(self):
        duration = time.time() - self.start_time
        avg_response = (sum(self.response_times) / len(self.response_times)) if self.response_times else 0
        return {
            'duration': duration,
            'requests': self.requests,
            'errors': self.errors,
            'avg_response_time': avg_response
        }
