from aiohttp import web
import aiohttp_debugtoolbar  #debug 

# from init_db import pg_context
from apps.settings import config
from routes import urlpatterns

from apps.v1.middlewares import Middleware


def setup_routes(application):
    urlpatterns(application)  


def setup_middlewares(app):
    mdw = Middleware()
    app.middlewares.append(mdw.midlleware)
    


def setup_external_libraries(application: web.Application) -> None:
    application['config'] = config
    aiohttp_debugtoolbar.setup(application)
    # application.cleanup_ctx.append(pg_context)

def setup_app(application):
    setup_middlewares(application)
    setup_external_libraries(application)  
    setup_routes(application) 
    

app = web.Application()

setup_app(application=app)


if __name__ == '__main__':

    web.run_app(app)
