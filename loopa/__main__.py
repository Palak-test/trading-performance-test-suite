"""
__main__.py

Entry point for loopa load testing tool.
"""

from loopa.argument_parser import get_args
from loopa.env import get_env

if __name__ == "__main__":
    args = get_args()
    env = get_env()
    print(f"Starting loopa with host={env['host']} users={env['users']} run_time={env['run_time']}")
