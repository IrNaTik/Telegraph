import jwt
from .errors import HandlerStatusError
from yaml import safe_load
from database_work.work_with_db import db_provider

class Token:

    def __init__(self) -> None:
        with open('config/jwt.yaml') as f:
            self.JWT_CONF = safe_load(f)


    async def check_jwt_token(self, request):
        try:

            asses_token = request.headers['Authorization'].split(' ')[1]
            decoded = jwt.decode(asses_token, self.JWT_CONF['ATsecret'], algorithms=["HS256"])
            
            return decoded.get('user_id') 
        except jwt.ExpiredSignatureError:
            print("exp time")
            raise HandlerStatusError(401)
        except jwt.InvalidSignatureError:

            raise HandlerStatusError(404)

    
