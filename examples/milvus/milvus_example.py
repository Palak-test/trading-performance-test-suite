# milvus_example.py

"""
Example of a Milvus client for loopa.
"""

from pymilvus import connections

class LoopaMilvusClient:
    def __init__(self, host):
        connections.connect(host=host)

    def search(self):
        # Example search call
        pass

if __name__ == "__main__":
    client = LoopaMilvusClient("localhost")
    # Example: client.search()
