from aiohttp import web
from aiohttp_jwt import JWTMiddleware
import aiohttp_debugtoolbar  #debug 

from apps.settings import config
from apps.auth.models import pg_context
from apps.auth.routes import urlpatterns
from apps.auth.models import pg_context



def setup_routes(application):
    urlpatterns(application)  

def setup_external_libraries(application: web.Application) -> None:
    application['config'] = config
    aiohttp_debugtoolbar.setup(application)
    application.cleanup_ctx.append(pg_context)

def setup_app(application):
    setup_external_libraries(application)  
    setup_routes(application) 


app = web.Application()

setup_app(application=app)


if __name__ == '__main__':
    web.run_app(app)
