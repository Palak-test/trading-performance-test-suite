"""
dispatch.py

Handles task dispatching for loopa load testing tool.
"""

class Dispatcher:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        for task in self.tasks:
            task()
