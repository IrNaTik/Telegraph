from aiohttp import web
from .views import TokenView

def utlpatterns(app):
    app.add_routes([web.view('/api/refresh', TokenView)])