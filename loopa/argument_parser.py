"""
argument_parser.py

Handles command-line arguments for loopa load testing tool.
"""

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Loopa load testing tool")
    parser.add_argument('--host', type=str, help='Target host URL')
    parser.add_argument('--users', type=int, default=1, help='Number of users')
    parser.add_argument('--run-time', type=str, help='Test duration')
    return parser.parse_args()
