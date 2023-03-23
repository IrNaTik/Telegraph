import jwt
from datetime import datetime, timedelta
from aiohttp import web
from yaml import safe_load

from database_work.work_with_db import db_provider

class TokenView(web.View):

    def __init__(self, request: web.Request) -> None:

        with open('config/jwt.yaml') as f:
            self.JWT_CONF = safe_load(f)
        
        self.POST = {
            'Access-Control-Allow-Origin': 'http://localhost:3000'
        }
        
        self.OPTIONS = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Credentials': 'true',
            'Allow': 'OPTIONS, POST',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': '''Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Allow-Origin, Access-Control-Request-Headers, Authorization'''
        }
        super().__init__(request)

    async def post(self):
        try: 
            cookies = self.request.headers['Cookie']
            refr = cookies[cookies.find('Ref')+4:]
        except KeyError:
            print("cookie is not aviable")
        
        decoded = jwt.decode(refr, self.JWT_CONF['RTsecret'], algorithms=['HS256']) # if error raise 403 
        user_id = decoded.get('user_id')
        
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
        
        data = {'AssesToken': asses_token}

        resp = web.json_response(data=data, status=200, headers=self.OPTIONS)        
        resp.set_cookie(name="Ref", value=refresh_token, httponly=True ,
                        max_age=self.JWT_CONF['exp_refresh'] * 60)
        
        return resp

    async def options(self):
        return web.Response(headers=self.OPTIONS)