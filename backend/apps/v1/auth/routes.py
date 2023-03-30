from aiohttp import web
from .views import AuthView


def urlpatterns(app: web.Application):
    app.add_routes([web.view('/login', AuthView)])
