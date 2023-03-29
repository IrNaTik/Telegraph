import jwt
import json
import yaml

from aiohttp import web
from apps.logics.headers import LOGIN_OPTIONS
from datetime import datetime, timedelta

# from .models import user

from database_work import db_provider



class AuthView(web.View):
    
    def __init__(self, request: web.Request) -> None:
    
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = yaml.safe_load(f)

        super().__init__(request)

    async def valid_token(self):

        try:
            asess_token = self.request.headers['Authorization']
            asess_token = asess_token.split(' ')[1]
            
            decoded = False
            try:
                decoded = jwt.decode(asess_token, self.JWT_CONF['ATsecret'], algorithms=["HS256"])
                
                try:
                    user_id = decoded.get('user_id')
                    data = await db_provider.user.get_access_data_table(user_id)
                except Exception as e:
                    print(e)
                    return False 
                
            except jwt.exceptions.InvalidSignatureError:
                print("Not valid token")
                return False
            except jwt.exceptions.ExpiredSignatureError:
                    print("exp time")
                    try:       
                        cookies = self.request.headers['Cookie']
                        refr = cookies[cookies.find('Ref')+4:]
                    except KeyError:
                        return False
                    
                    try:
                        jwt.decode(refr, self.JWT_CONF['RTsecret'], algorithms=["HS256"]) # if user_exists(): # Work with database
                        return True
                    except jwt.ExpiredSignatureError:
                        return False # Required to enter login with passwordу
                    except jwt.InvalidSignatureError:
                        return False
                    
            except Exception as e:
                print('Suck')
                print(type(e), e)
            
            if decoded:
                return True      
        except KeyError:
            print('key error')
            return False
        

    async def get(self):
        if await self.valid_token():
            return web.json_response(headers=self.GET, status=200)  # redirect to home
        else:
            return web.json_response(headers=self.OPTIONS, status=401)
        


    async def post(self):
        
        resp = await self.request.content.read()  
        result = json.loads(resp.decode('utf-8')) 

        login = result['login']
        password = result['password']
        
        user = await db_provider.user.add_user(login, password, "Ignat")        
        user = await db_provider.user.get_user_id_by_login(login) 
        print(user)
        if user['error']:
            return web.json_response(data={'message': 'User is not defined'},headers=LOGIN_OPTIONS, status=401)

        user_id = user['user_id']
        ATpayload = {
            'user_id': user_id,
            'exp': datetime.utcnow() +
            timedelta(seconds=self.JWT_CONF['exp_asses'])
        }

        RTpayload = {
            'user_id': user_id,
            'exp': datetime.utcnow() +
                timedelta(minutes=self.JWT_CONF['exp_refresh'])
        }

        jwt_token = jwt.encode(ATpayload, self.JWT_CONF['ATsecret'], self.JWT_CONF['algoritm'])
        refresh_token = jwt.encode(RTpayload, self.JWT_CONF['RTsecret'], self.JWT_CONF['algoritm'])
        
        await db_provider.user.update_access_data_table(login, user_id, refresh_token)

        value = {
            'AssesToken': jwt_token
        }
        
        resp = web.json_response(data=value, headers=LOGIN_OPTIONS)
        resp.set_cookie(name="Ref", value=refresh_token, httponly=True ,
                        max_age=self.JWT_CONF['exp_refresh'] * 60)

        return resp


    async def options(self):
        return web.Response(headers=LOGIN_OPTIONS)

