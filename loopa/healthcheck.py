"""
healthcheck.py

Provides a health check endpoint for loopa load testing tool.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
        else:
            self.send_response(404)
            self.end_headers()


def run_healthcheck_server(port=8080):
    server = HTTPServer(("", port), HealthCheckHandler)
    print(f"Healthcheck server running on port {port}")
    server.serve_forever()
