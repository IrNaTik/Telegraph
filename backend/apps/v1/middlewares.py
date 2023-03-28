from aiohttp import  web
from typing import Callable, Any, Union
from apps.logics.headers import OPTIONS
from apps.logics.valid_token import Token, HandlerStatusError

class Middleware:
    
    def __init__(self) -> None:
        self.status = 500
        self.body = {}

    @web.middleware
    async def midlleware(self, request: web.Request, handler: Callable) -> web.Response:

        if request.rel_url.path == '/login' or request.rel_url.path == '/api/refresh':
            return handler(request)
        else:
            try:
                if request.method != 'OPTIONS':
                    user_id = await Token().check_jwt_token(request=request) # maybe userid write in request


                return await self.run_handler(handler=handler, request=request)

            except HandlerStatusError as hs:

                if hs.status == 401:
                    self.status = 401
                    self.body = {
                    'type': "token is not valid"
                    }
                elif hs.status == 404:
                    self.status = 401
                    self.body = {
                    'type': "token is invalid"
                    }

                return web.json_response(data=self.body, status=self.status, headers=OPTIONS)

            except Exception as e:
                self.status = 500
                self.body = self.get_error_body(e)
                print(e)  

                return web.json_response(data=self.body, status=self.status, headers=OPTIONS)


        
