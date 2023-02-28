from .views import index, registration, chat


def urlpatterns(app):
    app.router.add_get('/', index)
    app.router.add_get('/user', registration)
    app.router.add_get('/ws', chat)
    
    