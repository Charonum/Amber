import os
import subprocess
import sys
import tempfile
import time
import atexit
from flask import Flask, request, make_response
from contextlib import contextmanager

ram_alloc = open("amber-cfg.txt", "r").read().strip().replace("ram: ", "")
f = tempfile.TemporaryFile()

server = subprocess.Popen(
    'java -Xmx' + ram_alloc + 'g -Xms' + ram_alloc + 'g -jar server.jar nogui',
    shell=True,
    text=True,
    stdout=f,
    stdin=subprocess.PIPE,
    bufsize=1,
    universal_newlines=True,
)

presence = open("pid.txt", "w")
presence.write(str(os.getpid()))
presence.close()


def stop_server(now=True):
    if now:
        server.stdin.write('stop' + '\n')
        server.stdin.flush()
        server.kill()
        f.close()
    else:
        server.stdin.write('say The server is shutting down in 5 minutes!' + '\n')
        server.stdin.flush()
        time.sleep(300)
        server.stdin.write('stop' + '\n')
        server.stdin.flush()
        server.kill()
        f.close()


atexit.register(stop_server)

app = Flask(__name__)


@app.route('/command', methods=['POST'])
def command():
    data = request.json
    server.stdin.write(data['command'] + '\n')
    server.stdin.flush()
    if data['command'] == "stop":
        try:
            return "", 200
        finally:
            server.kill()
            f.close()
    else:
        return "", 200


@app.route("/log", methods=['GET'])
def log():
    f.seek(0)
    log_lines = f.read().decode('utf-8')
    response = make_response(log_lines, 200)
    response.mimetype = "text/plain"
    return response


app.run(port=5000)
