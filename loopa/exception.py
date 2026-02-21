"""
exception.py

Defines custom exceptions for loopa load testing tool.
"""

class LoopaError(Exception):
    pass

class LoopaConfigError(LoopaError):
    pass
