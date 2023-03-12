import jwt
import json
import yaml
from aiohttp import web
from multidict import CIMultiDictProxy
from datetime import datetime, timedelta

from .models import user

from database_work import db_provider



class AuthView(web.View):
    
    def __init__(self, request: web.Request) -> None:

        self.GET = {'Access-Control-Allow-Origin': 'http://localhost:3000',
                    'Access-Control-Allow-Credentials': 'true'}
        self.POST = {
            
                    }
        self.OPTIONS = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Credentials': 'true',
            'Allow': 'OPTIONS, GET, POST',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
            'Access-Control-Allow-Headers': '''Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization'''
        }
    
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = yaml.safe_load(f)

        super().__init__(request)

    def valid_token(self):
        
        try:
            asess_token = self.request.headers['Authorization']
            asess_token = asess_token.split(' ')[1]

            try:
                decoded = jwt.decode(asess_token, self.JWT_CONF['ATsecret'], algorithms=["HS256"])
                print(decoded)
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
            
            if decoded:
                return True      
        except KeyError:
            print('key error')
            return False
        

    async def get(self):
        if self.valid_token():
            return web.json_response(headers=self.GET, status=200)  # redirect to home
        else:
            return web.json_response(headers=self.OPTIONS, status=404)
        


    async def post(self):
        #get from db data
        #valid self.request.data login password

        ATpayload = {
            'user_id': 1,
            'exp': datetime.utcnow() +
            timedelta(minutes=self.JWT_CONF['exp_asses'])
        }

        RTpayload = {
            'user_id': 1,
            'exp': datetime.utcnow() +
                timedelta(minutes=self.JWT_CONF['exp_refresh'])
        }

        jwt_token = jwt.encode(ATpayload, self.JWT_CONF['ATsecret'], self.JWT_CONF['algoritm'])
        refresh_token = jwt.encode(RTpayload, self.JWT_CONF['RTsecret'], self.JWT_CONF['algoritm'])
        
        value = {
            'AssesToken': jwt_token
        }
        
        resp = web.json_response(data=value, headers=self.OPTIONS)


        resp.set_cookie(name="Ref", value=refresh_token, httponly=True ,
                        max_age=self.JWT_CONF['exp_refresh'] * 60)

        return resp


    async def options(self):
        return web.Response(headers=self.OPTIONS)

