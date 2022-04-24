#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.1.7"
PORT = 8000


class myHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            bytes("<html><body><h1>I lub ju, ji!</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "'+date+'"}\n', "utf-8"))


server = HTTPServer((HOST, PORT), myHTTP)
print("Server is now running on " + HOST + ":" + str(PORT))
server.serve_forever()
server.server_close()
print("The server is stopped!")
