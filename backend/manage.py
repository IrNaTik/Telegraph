from aiohttp import web
import aiohttp_debugtoolbar

from apps.settings import config
from apps.auth.models import pg_context
from apps.auth.routes import urlpatterns
from apps.auth.models import pg_context


app = web.Application()
aiohttp_debugtoolbar.setup(app)
app['config'] = config
urlpatterns(app)
app.cleanup_ctx.append(pg_context)


if __name__ == '__main__':
    web.run_app(app)

