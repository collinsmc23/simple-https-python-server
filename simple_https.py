from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class myHandler(BaseHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.end_headers()
          self.wfile.write(b'Communication Established\n')

httpd = HTTPServer(('IP ADDRESS', PORT_NUM), myHandler)

# Generate .key & .crt files using the openssl library. 
# Linux: openssl req -x509 -newkey rsa:2048 -keyout your_selfsigned.key -out your_selfsigned.crt -days 365
httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="your_selfsigned.key",
        certfile='your_selfsigned.crt', server_side=True)

httpd.serve_forever()
