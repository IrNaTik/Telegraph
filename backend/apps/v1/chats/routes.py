from aiohttp import web
from .views import websocket_chat, ChatPagination


def urlpatterns(app: web.Application):
    app.router.add_get('/ws/chat/', websocket_chat)
    app.add_routes([web.view('/message', ChatPagination)])
