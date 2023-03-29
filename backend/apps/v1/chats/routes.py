from .views import websocket_chat, GetChatWithUser, get_chat_existing


def urlpatterns(app):
    # app.router.add_get('/ws/chat/{chat_id:.*}', websocket_chat)
    app.router.add_get('/ws/chat/', websocket_chat)
<<<<<<< HEAD
    app.router.add_get('/get-chat-existing', get_chat_existing )
    
=======
    app.router.add_get('/chat/{chat_name:\d+}', GetChatWithUser)
>>>>>>> 377e2d3e21686852ea86d14c4e2cee15b00d6676
