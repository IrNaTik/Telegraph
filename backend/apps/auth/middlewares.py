import yaml 
import jwt
from aiohttp import web
from typing import Any, Callable


class Token_handler:

    def __init__(self) -> None:
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = yaml.safe_load(f)

    async def check_signature(self, request: web.Request):
        
        if request.method == "GET" or request.method == "OPTIONS":
        #  if request.rel_url == '\login':
            pass
            #check diff
        else:   
            tokens = dict(request.raw_headers)
            tokens = dict([(key.decode('utf-8'), value.decode('utf-8')) for key, value in tokens.items()])
            asses_token = tokens.get("Authorization").split(' ')[1]
            
            try:
                asses_token_data = jwt.decode(asses_token, self.JWT_CONF['ATsecret'], self.JWT_CONF['algoritm'])
            except:
                pass
                # raise 404

            user_id = asses_token_data['user_id']
            print(user_id)



    #check asses token 
    @web.middleware
    async def middleware(self, request: web.Request, handler: Callable):
        # await self.check_signature(request)
        resp = await handler(request)
        return resp

