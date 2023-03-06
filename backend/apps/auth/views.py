import jwt
import yaml
from aiohttp import web
from datetime import datetime, timedelta

from .models import user


class AuthView(web.View):
    def __init__(self, request: web.Request) -> None:

        self.GET = {'Access-Control-Allow-Origin': 'http://localhost:3000'}
        self.POST = {
            
                    }
        self.OPTIONS = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Credentials': 'true',
            'Allow': 'OPTIONS, GET, POST',
            'Access-Control-Allow-Headers': '''Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, 
                                               Set-Cookie'''
        }
    
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = yaml.safe_load(f)

        super().__init__(request)

    async def get(self):
        #MUST CHECK IF USER IS AUTORIZATED
        print('Good')
        print(self.request.headers)
        ss = {"Asd": "ASd"}
        return web.json_response(data = ss, headers=self.GET)


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
        
        resp = web.json_response(data=value, headers=self.POST)

        resp.set_cookie(name="Ref", value=refresh_token,
                        max_age=self.JWT_CONF['exp_refresh'] * 60)

        return resp


    async def options(self):
        return web.Response(headers=self.OPTIONS)

