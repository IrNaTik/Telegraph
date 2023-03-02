from aiohttp import web
from .views import AuthView


def urlpatterns(app):
    app.add_routes([web.view('/login', AuthView)
                    ])