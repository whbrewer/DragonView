import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from sys import argv

PORT = int(os.getenv('DRAGONVIEW_PORT', 8000))
DATA_DIR = 'sim'
if len(argv) == 2:
    DATA_DIR = argv[1]

DATA_DIR = '/data/' + DATA_DIR

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/data'):
            self.path = DATA_DIR + self.path[len('/data'):]
        return SimpleHTTPRequestHandler.do_GET(self)

httpd = HTTPServer(("", PORT), MyHandler)
print(f"Serving at port {PORT}\nData Directory: {DATA_DIR}")
httpd.serve_forever()
