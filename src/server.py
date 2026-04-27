from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from routes.order_routes import handle_orders

PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/orders"):
            response = handle_orders("GET", self)
            self._set_headers()
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == "/orders":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body or "{}")

            response = handle_orders("POST", self, data)
            self._set_headers()
            self.wfile.write(json.dumps(response).encode())

def run():
    server = HTTPServer(("", PORT), RequestHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()