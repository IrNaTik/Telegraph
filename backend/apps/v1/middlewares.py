import jwt
from aiohttp import  web
from yaml import safe_load
from typing import Callable, Any, Union

from database_work.work_with_db import db_provider

class Token:


    def __init__(self) -> None:
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = safe_load(f)


    async def get_request_body(self, request: web.Request)-> Any:
        return await request.json()


    def get_error_body(self, request: web.Request, error: Exception) -> dict:

        return {"error_type": str(type(error)), "error_message": str(error)}


    async def run_handler(
        self, request: web.Request, handler: Callable
    )-> Any:
        """
            Run real handler
        """
        return await handler(request)


    async def get_response_body_and_status(
        self, request: web.Request, handler: Callable
    )-> Union[Any, int]:
        try:   
            responce_body = await self.run_handler(request, handler)
            status = 200
        except Exception as e:
            status = 400
            responce_body = f"Error: {e}"
            
        finally:
            return responce_body, status


    async def check_jwt_token(self, request: web.Request):
        try:
            asses_token = request.headers['Authorization'].split(' ')[1]
            decoded = jwt.decode(asses_token, self.JWT_CONF['ATsecret'], algorithms=["HS256"])
            print(decoded)
        except jwt.ExpiredSignatureError:
            print('time exp')
            try: 
                cookies = request.headers['Cookie']
                refr = cookies[cookies.find('Ref')+4:]
            except KeyError:
                print("cookie is not aviable")
 
            decoded = jwt.decode(refr, self.JWT_CONF['RTsecret'], algorithms=['HS256']) # if error raise 403 
            user_id = decoded.get('user_id')
            
            try: # must be on level db
                user_data = db_provider.user.get_access_data_table()
                date = request.headers['Date']
                print(date)
            except Exception as e:
                print(f"Error: {e}")

        except jwt.InvalidSignatureError:
            print('inv token')
        except Exception as e:
            print('standart error')
            print(f'Error: {e}')
            # error_body = self.get_error_body(request, e)
            
            # raise 403 error


    @web.middleware
    async def middleware(self, request: web.Request, handler: Callable):
        if request.rel_url.path == "/login":
            print(request.rel_url)
        elif  request.rel_url.path == '/ws/chat/':
            print(request.rel_url)
        else:
            # try: 
            #     request = await self.get_request_body(request)
            # except Exception as e:
            #     status = 400
            #     responce_body = f"Error: {e}"

            await self.check_jwt_token(request)

        return await handler(request)
