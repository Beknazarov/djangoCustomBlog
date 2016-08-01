from exceptions import RouteNotFoundException
from views import handle_404

ROUTE_NOT_FOUND_EXCEPTION_MESSAGE = 'Route for method {method} and path {path} not found'


class Router(object):
    def __init__(self):
        self.routes = []

    def handle(self, request):
        try:
            handler = self._get_handler_for_path(request.command, request.path)
            handler(request)
        except RouteNotFoundException:
            handle_404(request)

    def register_routes(self, routes):
        if type(routes) != list:
            raise TypeError("Routes must be list")
        self.routes.extend(routes)

    def _get_handler_for_path(self, method, path):
        for route in self.routes:
            if route.check_method_and_path(method, path):
                return route.get_handler()
        raise RouteNotFoundException(ROUTE_NOT_FOUND_EXCEPTION_MESSAGE.format(method=method, path=path))


class Url(object):
    def __init__(self, method, path, handler):
        self.method = method
        self.path = path
        self.handler = handler

    def get_handler(self):
        return self.handler

    def get_url(self):
        return self.path

    def check_method_and_path(self, method, path):
        if len(path.split("?")) > 1:
            path, url = path.split("?")[0], path.split("?")[1]
            print(len(url))
            print(url)
        else:
            path = path.split("?")[0]
        return self.method == method and self.path == path
