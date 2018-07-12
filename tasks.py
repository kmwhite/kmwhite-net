import os
import sys
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

from invoke import run, env, task

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


@task
def clean(ctx):
    if os.path.isdir(DEPLOY_PATH):
        run(f'rm -rf {env.deploy_path}')
        run(f'mkdir {env.deploy_path}')

@task
def build(ctx):
    run('pelican -s pelicanconf.py src/')

@task
def serve(ctx):
    os.chdir(env.deploy_path)

    PORT = 8000
    ADDRESS = '127.0.0.1'
    CONFIG = (ADDRESS, PORT)
    class AddressReuseTCPServer(TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(CONFIG, SimpleHTTPRequestHandler)

    sys.stderr.write(f'Serving on port {ADDRESS}:{PORT} ...\n')
    server.serve_forever()

@task
def regenerate(ctx):
    clean(ctx)
    build(ctx)
    serve(ctx)
