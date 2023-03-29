from .views import websocket_chat, GetChatWithUser, get_chat_existing


def urlpatterns(app):
    # app.router.add_get('/ws/chat/{chat_id:.*}', websocket_chat)
    app.router.add_get('/ws/chat/', websocket_chat)
    app.router.add_get('/get-chat-existing', get_chat_existing )
    
