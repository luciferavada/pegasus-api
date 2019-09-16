import os

from watchgod import run_process

from server import server

import handlers
import resource
import seed

def run():
    server.run(host='0.0.0.0', port=os.getenv('PORT', 8080), workers=1)

run_process('../server', run)
