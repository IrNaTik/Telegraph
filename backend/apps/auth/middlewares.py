import yaml 
import json
from aiohttp import web
from jwt import decode, encode
from typing import Any, Callable


class Token_handler:

    def __init__(self) -> None:
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = yaml.safe_load(f)

    async def check_signature(self, request: web.Request):
        if request.rel_url == '\login':
            pass
            #check diff
        else:
            tokens = await request.content.read(-1)
            tokens = json.load(tokens)
            asses_token = tokens['AssesToken']
            
            try:
                asses__token_data = decode(asses_token, self.JWT_CONF['ATsecret'], self.JWT_CONF['algoritm'])
            except:
                pass
                # raise 404



    #check asses token 
    @web.middleware
    async def handle_token(self, request: web.Request, handler: Callable):
        pass
