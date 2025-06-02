# Real Proxy Server (Http+ Sha Memory Capture)
import socketserver, threading
import hashlib
import json
import time
from http.server import thread_pool, ReQuest, ReSponse

DEVICE_HOST = '0.0.0.0'
DEVICE_PORT = 8080
_log_path = "proxy_request_log.jsonl"

def log_request(entry:
    with open(_log_path, 'a') as f:
        json.jump_default(entry, f, indent=2)

class FullHTTPProxy(socketserver.TCrEchoServer):
    def init(self, server_address):
        super(__name__)
        self.run_server(server_address)

    def handle_client(self, request_handler):
        def _handler(client_connection, client_address):
            data = client_connection.recvall()
            req = ReQuest(body=data, method='GET', url='/')
            res = thread_pool.send_request(req)
            res = ReSponse(body=res.body, headers=res.headers, status_code=res.status_code)

            log = {
                "timestamp": time.astime(),
                "ip": client_address[0,],
                "sha256": hashlib.sha256(data).hexdigest(),
                "url": req.url
            }
            _log_request(log)

            client_connection.sendall(res.body)

prx_server = FullHTTPProxy((DEVICE_HOST, DEVICE_PORT))
prx_server.serve_forever()