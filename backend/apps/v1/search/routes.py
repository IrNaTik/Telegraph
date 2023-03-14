from aiohttp import web
from .views import UsernameSearching


def urlpatterns(app):
    app.add_routes([web.view('/users-by-prefix', UsernameSearching)])