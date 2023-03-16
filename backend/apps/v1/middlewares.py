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

    def get_error_body(self, error: Exception) -> dict:
        return {"error_type": str(type(error)), "error_message": str(error)}


    async def run_handler(
        self, request: web.Request, handler: Callable
    )-> Any:
        """
            Run real handler
        """
        return await handler(request)


    # async def get_response_body_and_status(
    #     self, request: web.Request, handler: Callable
    # )-> Union[Any, int]:
    #     try:   
    #         responce_body = await self.run_handler(request, handler)
    #         status = 200
    #     except Exception as e:
    #         status = 400
    #         responce_body = f"Error: {e}"
            
    #     finally:
    #         return responce_body, status


    @web.middleware
    async def midlleware(
        self, request: web.Request, handler: Callable
        ) -> web.Response:

        if request.rel_url.path == "/login":
            return self.run_handler(request, handler)
        elif  request.rel_url.path == '/ws/chat/':
            return self.run_handler(request, handler)
        else:
            
            # response_body, status = self.get_response_body_and_status(request=request, handler=handler)
            try:
                # user_id = await Token().check_jwt_token(request=request) # maybe userid write in request
                # print(user_id)
                
                response = await handler(request)
                # print(body, status)
                
            # except HandlerStatusError as hs:

            #     if hs == 401:
            #         self.status = 401
            #         self.body = self.get_error_body(HandlerStatusError)
            #     elif hs == 404:
            #         self.status = 401
            #         self.body = self.get_error_body(HandlerStatusError)
            
            except Exception as e:
                self.status = 500
                self.body = self.get_error_body(Exception)
                print(e)

            finally:
                return web.json_response(data=self.body, status=self.status)


class Token:

    def __init__(self) -> None:
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = safe_load(f)


    async def check_jwt_token(self, request: web.Request):
        try:
            asses_token = request.headers['Authorization'].split(' ')[1]
            decoded = jwt.decode(asses_token, self.JWT_CONF['ATsecret'], algorithms=["HS256"])
            
            return await decoded.get('user_id') 
        except jwt.ExpiredSignatureError:

            raise HandlerStatusError(401)
        except jwt.InvalidSignatureError:

            raise HandlerStatusError(404)
        except Exception as e:

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
    