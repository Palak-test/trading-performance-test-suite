# custom_xmlrpc_client_example.py

"""
Example of a custom XML-RPC client for loopa.
"""

import xmlrpc.client

class CustomXMLRPCClient:
    def __init__(self, url):
        self.server = xmlrpc.client.ServerProxy(url)

    def call_method(self, method, *args):
        return getattr(self.server, method)(*args)

if __name__ == "__main__":
    client = CustomXMLRPCClient("http://localhost:8000")
    # Example: client.call_method('ping')
