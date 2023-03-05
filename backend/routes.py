from apps.auth.routes import urlpatterns as auth_routes
from apps.chats.routes import urlpatterns as chats_routes



def urlpatterns(app):
    chats_routes(app)
    auth_routes(app)
    
    