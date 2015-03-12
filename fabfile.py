from fabric.api import local
import os
import shutil
import sys
import SimpleHTTPServer
import SocketServer

# Port for `serve`
PORT = 5000

def build():
    """Build local version of site"""
    # Generate the static content
    # -v for verbose mode
    # -D for debug output
    # -s for specifying a custom settings file
    local('pelican -s settings.py src/')

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s settings.py src/')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir('output')

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def publish():
    """Publish to Heroku"""
    build()
    os.chdir('output')
    local('git commit -a && git push')
