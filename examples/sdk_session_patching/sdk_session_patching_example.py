# sdk_session_patching_example.py

"""
Example of SDK session patching for loopa.
"""

class SDKSession:
    def patch(self):
        print("Session patched!")

if __name__ == "__main__":
    session = SDKSession()
    session.patch()
