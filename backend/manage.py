from aiohttp import web
from aiohttp_jwt import JWTMiddleware
import aiohttp_debugtoolbar  #debug 

# from init_db import pg_context
from apps.settings import config
from routes import urlpatterns





def setup_routes(application):
    urlpatterns(application)  
    print(app.router.routes().__iter__())
    for rout in app.router.routes().__iter__():
        print(rout)
    

def setup_external_libraries(application: web.Application) -> None:
    application['config'] = config
    aiohttp_debugtoolbar.setup(application)
    # application.cleanup_ctx.append(pg_context)

def setup_app(application):
    setup_external_libraries(application)  
    setup_routes(application) 
    

app = web.Application()

setup_app(application=app)


if __name__ == '__main__':
    web.run_app(app)
