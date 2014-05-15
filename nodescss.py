import argparse
import subprocess
import SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

parser = argparse.ArgumentParser(description='NodeSCSS on the Server!')
parser.add_argument("--ip", default="127.0.0.1",
  help="Listen ip")
parser.add_argument("--port", type=int, default=1234,
  help="Listen port")
parser.add_argument("filename", type=str, help="scss file")
args = parser.parse_args()

DISPATCH = """
@import '%s';

$request: %s;

body {
    content: handle_request($request);
}
"""
REQUEST = """
(
    path: '{path}',
    user_agent: '{user_agent}'
)
"""


class NodeSCSS(SimpleHTTPRequestHandler):
    """
    Pass request to node.scss handle_request
    """

    def do_GET(self):

        proc = subprocess.Popen(['scss', '-s'],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE)

        src = DISPATCH % (
            args.filename,
            REQUEST.format(
                path=self.path,
                user_agent=self.headers.get('User-Agent', '')))
        proc.stdin.write(src)
        stdout, stderr = proc.communicate()
        proc.stdin.close()

        if proc.returncode != 0:
            self.send_response(500)
            self.send_header('Content-Type', 'text/plain')
            response = stderr + '\n' + src
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            response = stdout[stdout.find('"')+1:stdout.rfind('"')]

        self.end_headers()

        self.wfile.write(response)
        self.wfile.close()

SocketServer.TCPServer((args.ip, args.port), NodeSCSS).serve_forever()
