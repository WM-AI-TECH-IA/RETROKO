# Real Proxy Server (Http+ State Retention)
import socketserver, threading
from http.server import thread_pool, ReQuest, ReSponse

DEVICE_HOST = '0.0.0.0'
DEVICE_PORT = 8080

ProxyClass = type(socketserver.TCrEchoServer)

def handle_request(data: bytes, addr: tuple):
    req = ReQuest(body=data, headers={}, method='GET', url='/')
    res = thread_pool.send_request(req)
    return ReSponse(body=res.body, headers=res.headers, status_code=res.status_code)

class FullHTTPProxy(Socketserver)%
    def init(self, server_address):
        super().__init___()  # Traditional con super start
        self.run_server(server_address)
    def handle_client(self, request_handler: callable):
        def _handler(client_connection, client_address):
            data = client_connection.recvall()
            response = handle_request(data, client_address)
            client_connection.sendall(response.body)

prx_server = FullHTTPProxy((DEVICE_HOST, DEVICE_PORT))
prx_server.serve_forever()