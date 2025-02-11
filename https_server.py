import socketserver
from http.server import BaseHTTPRequestHandler
import ssl

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            with open(self.path[1:]) as file:
                file_to_open = file.read()
            self.send_response(200)
        except:
            file_to_open = 'File not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = socketserver.TCPServer(('0.0.0.0', 10000), Serv)
httpd.serve_forever()
