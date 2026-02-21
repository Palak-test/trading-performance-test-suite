# qdrant_example.py

"""
Example of a Qdrant client for loopa.
"""

from qdrant_client import QdrantClient

class LoopaQdrantClient:
    def __init__(self, host):
        self.client = QdrantClient(host=host)

    def search(self):
        # Example search call
        pass

if __name__ == "__main__":
    client = LoopaQdrantClient("localhost")
    # Example: client.search()
