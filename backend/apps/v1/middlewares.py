import jwt

from aiohttp import  web
from yaml import safe_load
from typing import Callable, Any, Union


from database_work.work_with_db import db_provider

class Middleware:
    """
        response_bosy is dict
    """
    def __init__(self) -> None:
        self.body = {}
        self.status = 500
        self.headers = {'Access-Control-Allow-Origin': 'http://localhost:3000',
                    'Access-Control-Allow-Credentials': 'true',
        }

    def get_error_body(self, error: Exception) -> dict:
        return {"error_type": str(type(error)), "error_message": str(error)}


    async def run_handler(
        self, request: web.Request, handler: Callable
    )-> Any:
        """
            Run real handler
        """
        return await handler(request)

    @web.middleware
    async def midlleware(
        self, request: web.Request, handler: Callable
        ) -> web.Response:

        if request.rel_url.path == "/login":    
            return await self.run_handler(request, handler)
        elif  request.rel_url.path == '/ws/chat/':
            return await self.run_handler(request, handler)
        elif  request.rel_url.path == '/api/refresh':
            return await self.run_handler(request, handler)
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
                
                return web.json_response(data=self.body, status=self.status, headers=self.headers)
            
            except Exception as e:
                self.status = 500
                self.body = self.get_error_body(e)
                print(e)  

                return web.json_response(data=self.body, status=self.status, headers=self.headers)


class Token:

    def __init__(self) -> None:
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = safe_load(f)


    async def check_jwt_token(self, request: web.Request):
        try:

            asses_token = request.headers['Authorization'].split(' ')[1]
            decoded = jwt.decode(asses_token, self.JWT_CONF['ATsecret'], algorithms=["HS256"])
            
            return decoded.get('user_id') 
        except jwt.ExpiredSignatureError:
            print("exp time")
            raise HandlerStatusError(401)
        except jwt.InvalidSignatureError:

            raise HandlerStatusError(404)
        
# move to a separate module
#exmpl: https://github.com/encode/django-rest-framework/blob/19655edbf782aa1fbdd7f8cd56ff9e0b7786ad3c/rest_framework/exceptions.py#L140
class HandlerStatusError(Exception): 
    def __init__(self, *args: object) -> None:
        if args:
            self.status = args[0]

    def __str__(self) -> str:
        if self.status:
            return f'{self.status}'
    