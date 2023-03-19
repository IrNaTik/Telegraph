import jwt
import json
import yaml
from aiohttp import web
from datetime import datetime, timedelta

from database_work import db_provider



class AuthView(web.View):
    
    def __init__(self, request: web.Request) -> None:
        self.OPTIONS = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Credentials': 'true',
            'Allow': 'OPTIONS, GET, POST',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': '''Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization'''
        }
    
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = yaml.safe_load(f)

        super().__init__(request)


    async def post(self):
        resp = await self.request.content.read() 
        result = json.loads(resp.decode('utf-8')) # handle error


        login = result['login']
        password = result['password']
        
        # #only for test
        # try:
        #     user_id = await db_provider.user.get_user_id(login) 
        # except:
        resp = await db_provider.user.add_user(login, password)
        print(resp)
        if  resp['error']:
            if resp['type'] == 'IncorrectFormat':
                pass
        
        user = await db_provider.user.get_user_id(login)
        
        if  not user['error']:
            user_id = user['user_id']
        else: 
            user_id = 1 #handler error

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
        
        resp = web.json_response(data=value, headers=self.OPTIONS)
        resp.set_cookie(name="Ref", value=refresh_token, httponly=True ,
                        max_age=self.JWT_CONF['exp_refresh'] * 60)

        return resp


    async def options(self):
        return web.Response(headers=self.OPTIONS)

