"""
env.py

Manages environment configuration for loopa load testing tool.
"""

import os

def get_env():
    return {
        'host': os.getenv('LOOPA_HOST', 'http://localhost'),
        'users': int(os.getenv('LOOPA_USERS', 1)),
        'run_time': os.getenv('LOOPA_RUN_TIME', '1m')
    }
