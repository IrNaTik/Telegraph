from aiohttp import web

from handlers.routes import urlpatterns

app = web.Application()
urlpatterns(app)
web.run_app()
