from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from routes.order_routes import handle_request

PORT = 8000


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        response = handle_request(self.path, "GET", None)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length).decode()

        response = handle_request(self.path, "POST", body)

        self.send_response(201)
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    print(f"Starting server on port {PORT}")
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()