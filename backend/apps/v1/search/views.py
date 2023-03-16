from aiohttp import web
from database_work import db_provider


class UsernameSearching(web.View):
    def __init__(self,request) -> None:
        
        self.GET = {'Access-Control-Allow-Origin': 'http://localhost:3000',
                    'Access-Control-Allow-Credentials': 'true',
                    'Allow': 'OPTIONS, GET, POST',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
            'Access-Control-Allow-Headers': '''Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization''',
            'Access-Control-Request-Headers': '''prefix'''
        }
        self.POST = {
            
                    }
        self.OPTIONS = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Credentials': 'true',
            'Allow': 'OPTIONS, GET, POST',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
            'Access-Control-Allow-Headers': '''Content-Type, prefix, Authorization, Date''',
            'Access-Control-Request-Headers': '''prefix, Authorization'''
        }
        super().__init__(request)

    async def get(self):
        prefix = self.request.headers['prefix']
        users = await db_provider.user.get_by_prefix(prefix)
        logins = [user.login for user in users]
        print(logins)

        return [logins, 200]
            

    async def options(self):
        return web.Response(headers=self.OPTIONS)
    
    

    

