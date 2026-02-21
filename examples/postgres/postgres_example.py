# postgres_example.py

"""
Example of a PostgreSQL client for loopa.
"""

import psycopg2

class LoopaPostgresClient:
    def __init__(self, dsn):
        self.conn = psycopg2.connect(dsn)

    def query(self, sql):
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

if __name__ == "__main__":
    client = LoopaPostgresClient("dbname=test user=postgres")
    # Example: client.query('SELECT * FROM test_table')
