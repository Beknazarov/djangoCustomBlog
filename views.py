from http import HTTPStatus

from template_code.template import Template


def handle_404(request):
    # context = {}
    # url_split = str(request.path).split("?")
    # if len(url_split) > 1:
    #     url = url_split[1]
    #     context = {'not-found': 'File Has found'}
    #     f = open('db/database.json', 'w')
    #     f.write(url)
    #     f.close()
    # else:
    #     pass
    context = {'not-found': 'File Not found'}

    html = Template('404.html', context).render()
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))

    return request


def handle_index(request):
    context = {'variable': 'Hello world2'}

    html = Template('index.html', context).render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def login_vew(request):
    context = {}
    html = Template('login.html', context).render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request
