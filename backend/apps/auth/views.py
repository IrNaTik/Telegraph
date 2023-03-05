import jwt
import yaml
from aiohttp import web, web_ws
from datetime import datetime, timedelta
import json

from .models import user

with open('config/jwt.yaml') as f:
    JWT_CONF = yaml.safe_load(f)

# class ResponseBusted(web.Response):
#     def __init__(self, text, status):
#         super().__init__(text=text, status=status,
#                          headers={'Access-Control-Allow-Origin': 'http://localhost:3000'})

# def j_response(data, status = 200):
#     return web.json_response(data=data,
#                                 headers=)

class AuthView(web.View):

    async def get(self):
        #MUST CHECK IF USER IS AUTORIZATED
        ss = {"data": "test"}
        return web.json_response(data = ss)


    async def post(self):
        #check valid user
        #get from db data   

        ATpayload = {
            'user_id': 1,
            'exp': datetime.utcnow() +
            timedelta(minutes=JWT_CONF['exp_asses'])
        }

        RTpayload = {
            'user_id': 1,
            'exp': datetime.utcnow() +
                timedelta(minutes=JWT_CONF['exp_refresh'])
        }
        jwt_token = jwt.encode(ATpayload, JWT_CONF['ATsecret'], JWT_CONF['algoritm'])
        refresh_token = jwt.encode(RTpayload, JWT_CONF['RTsecret'], JWT_CONF['algoritm'])
        
        resp = {
            "AssesToken":  jwt_token,
            "RefreshToken": refresh_token
        }

        return  web.json_response(resp)