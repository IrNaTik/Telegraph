from .views import websocket_chat, GetChatWithUser


def urlpatterns(app):
    # app.router.add_get('/ws/chat/{chat_id:.*}', websocket_chat)
    app.router.add_get('/ws/chat/', websocket_chat)
    app.router.add_get('/chat/{chat_name:\d+}', GetChatWithUser)