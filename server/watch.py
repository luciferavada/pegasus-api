import os

from watchgod import run_process

def run():
    import handlers
    import resource
    import seed

    from server import server

    server.run(host='0.0.0.0', port=os.getenv('PORT', 8080), workers=1)

run_process('../server', run)
