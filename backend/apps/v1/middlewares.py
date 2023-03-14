import jwt

from aiohttp import  web
from yaml import safe_load
from typing import Callable, Any, Union
from datetime import datetime, timedelta

from database_work.work_with_db import db_provider

class Middleware:
    """
        response_bosy is dict
    """

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


    @web.middleware
    async def midlleware(
        self, request: web.Request, handler: Callable
        ) -> web.Response:

        if request.rel_url.path == "/login":
            return self.run_handler(request, handler)
        elif  request.rel_url.path == '/ws/chat/':
            return self.run_handler(request, handler)
        else:
            
            # response_body, status = self.get_response_body_and_status(request, handler)
            # response, refresh_token = Token(response=response_body)
            resp = web.Response(body="Asd")
            resp.body.set_content_disposition('dsa', name='asd')
            print(resp.body.write())
            return resp
            # return resp
            #  if refresh_token == '':

            # else:
            #     resp = web.Response(body=response_body)
            #     resp.set_cookie(name="Ref", value=refresh_token, httponly=True ,
            #             max_age=self.JWT_CONF['exp_refresh'] * 60)








class Token:

    def __init__(self, response, status: int) -> None:
        self.resp = web.Response(bosy=response, status=status)

        with open('config/jwt.yaml') as f:
            self.JWT_CONF = safe_load(f)


    async def check_jwt_token(self, request: web.Request):
        try:
            asses_token = request.headers['Authorization'].split(' ')[1]
            decoded = jwt.decode(asses_token, self.JWT_CONF['ATsecret'], algorithms=["HS256"])
            print(asses_token)
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
                user_data = await db_provider.user.get_access_data_table(user_id=user_id)
                date = datetime.utcnow() # must have date type
                
                ATpayload = {
                    'user_id': user_id,
                    'exp': datetime.utcnow() + timedelta(seconds=self.JWT_CONF['exp_asses'])
                }

                RTpayload = {
                    'user_id': user_id,
                    'exp': datetime.utcnow() + timedelta(minutes=self.JWT_CONF['exp_refresh']) 
                }

                asses_token = jwt.encode(ATpayload, self.JWT_CONF['ATsecret'], self.JWT_CONF['algoritm'])
                refresh_token = jwt.encode(RTpayload, self.JWT_CONF['RTsecret'], self.JWT_CONF['algoritm'])
                
                await db_provider.user.update_access_data_table(user_id=user_id, last_visit=date, refresh_token=refresh_token)
                
                self.resp.body()

            except Exception as e:
                print(f"Error: {e}")

        except jwt.InvalidSignatureError:
            print('inv token')
        except Exception as e:
            print('standart error')
            print(f'Error: {e}')
            # error_body = self.get_error_body(request, e)
            
            # raise 403 error
    
        finally:
            return self.response, ''
