from http.server import BaseHTTPRequestHandler

from router import Router
from urls import patterns


class myHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.router = Router()
        self.router.register_routes(patterns)
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.router.handle(request=self)
        return

    def do_POST(self):
        pass

    def do_HEAD(self):
        pass

    def do_PUT(self):
        pass
