from apps.auth.routes import urlpatterns as auth_routes
from apps.chats.routes import urlpatterns as chats_routes
from apps.search.routes import urlpatterns as search_routes



def urlpatterns(app):
    chats_routes(app)
    auth_routes(app)
    search_routes(app)
    