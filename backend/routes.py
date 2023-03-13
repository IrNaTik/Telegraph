from apps.v1.auth.routes import urlpatterns as auth_routes
from apps.v1.chats.routes import urlpatterns as chats_routes
from apps.v1.search.routes import urlpatterns as search_routes



def urlpatterns(app):
    chats_routes(app)
    auth_routes(app)
    search_routes(app)
    