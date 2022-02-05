#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

# httpd = HTTPServer(('172.17.0.3', 5555), BaseHTTPRequestHandler)

class myHandler(BaseHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.end_headers()
          self.wfile.write(b'Communication Established\n')

httpd = HTTPServer(('172.17.0.3', 5555), myHandler)


httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="/home/7028596/nginx_selfsigned.key",
        certfile='/home/7028596/nginx_selfsigned.crt', server_side=True)

httpd.serve_forever()
