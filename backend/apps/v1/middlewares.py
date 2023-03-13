from aiohttp import  web
from yaml import safe_load
import jwt


from typing import Callable

class Token:

    def __init__(self) -> None:
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = safe_load(f)

    async def check_jwt_token(self, request: web.Request):
        if (request.rel_url.path == "/login"):
            print(request.rel_url)
        else:
            
            try:
                asses_token = request.headers['Authorization']
                print(asses_token)
                jwt.decode()
            except jwt.ExpiredSignatureError:
                pass
                # try:
            except jwt.InvalidSignatureError:
                pass
            except:
                pass # raise 403 error


    @web.middleware
    async def middleware(self, request: web.Request, handler: Callable):
        await self.check_jwt_token(request)
        responce = await handler(request)

        return responce 
