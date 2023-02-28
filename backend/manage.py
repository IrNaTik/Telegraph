from aiohttp import web
import aiohttp_debugtoolbar


from apps.settings import config
from apps.auth.models import pg_context
from apps.auth.routes import urlpatterns
from apps.auth.models import pg_context


def setup_routes(application):
    urlpatterns(application)  

def setup_external_libraries(application: web.Application) -> None:
    # настройки внешних библиотек
    pass

def setup_app(application):
    setup_external_libraries(application)  
    setup_routes(application) 


app = web.Application()
aiohttp_debugtoolbar.setup(app)
app['config'] = config
urlpatterns(app)
app.cleanup_ctx.append(pg_context)


if __name__ == '__main__':
    web.run_app(app)
