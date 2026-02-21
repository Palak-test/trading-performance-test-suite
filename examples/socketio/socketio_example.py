# socketio_example.py

"""
Example of a Socket.IO client for loopa.
"""

import socketio

class LoopaSocketIOClient:
    def __init__(self, url):
        self.sio = socketio.Client()
        self.sio.connect(url)

    def emit(self, event, data):
        self.sio.emit(event, data)

if __name__ == "__main__":
    client = LoopaSocketIOClient("http://localhost:5000")
    client.emit("test_event", {"msg": "Hello, Socket.IO!"})
