import views
from method import HTTP_METHODS
from router import Url

patterns = [
    Url(HTTP_METHODS.GET, '/', views.handle_index),
    Url(HTTP_METHODS.GET, '/login/', views.login_vew)
]
