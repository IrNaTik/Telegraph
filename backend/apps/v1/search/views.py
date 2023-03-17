from aiohttp import web
from database_work import db_provider


class UsernameSearching(web.View):
    def __init__(self,request) -> None:
        
        # self.GET = {'Access-Control-Allow-Origin': 'http://localhost:3000',
        #             'Access-Control-Allow-Credentials': 'true',
        # }
        self.POST = {
            
                    }
        self.OPTIONS = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Request-Headers': 'authorization',
            'Access-Control-Request-Method': 'GET'
        }
        super().__init__(request)

    async def get(self):
        prefix = self.request.headers['prefix']
        users = await db_provider.user.get_by_prefix(prefix)
        print(users)
        logins = [user.login for user in users]
        print(logins)

        return [logins, 200]
            

    async def options(self):
        return web.Response(headers=self.OPTIONS, status=200)
    
    

    

