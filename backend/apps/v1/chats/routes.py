from .views import websocket_chat


def urlpatterns(app):
    # app.router.add_get('/ws/chat/{chat_id:.*}', websocket_chat)
    app.router.add_get('/ws/chat/', websocket_chat)
