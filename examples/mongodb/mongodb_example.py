# mongodb_example.py

"""
Example of a MongoDB client for loopa.
"""

from pymongo import MongoClient

class LoopaMongoClient:
    def __init__(self, uri):
        self.client = MongoClient(uri)

    def find(self, db, collection):
        return self.client[db][collection].find()

if __name__ == "__main__":
    client = LoopaMongoClient("mongodb://localhost:27017")
    # Example: client.find('testdb', 'testcol')
