from aiohttp import web

from apps.auth.routes import urlpatterns

app = web.Application()
urlpatterns(app)
web.run_app(app)
