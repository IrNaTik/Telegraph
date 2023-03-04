from .views import AuthView


def urlpatterns(app):
    app.router.add_get('/login', AuthView)
    
