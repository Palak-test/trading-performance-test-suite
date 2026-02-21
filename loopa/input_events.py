"""
input_events.py

Handles input events for loopa load testing tool.
"""

class InputEvent:
    def __init__(self, name):
        self.name = name
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def trigger(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)
