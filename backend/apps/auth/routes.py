from .views import index


def urlpatterns(app):
    app.router.add_get('/', index)
    