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
            'Access-Control-Request-Headers': 'Authorization, prefix',
            'Access-Control-Request-Method': 'GET',
            'Access-Control-Allow-Credentials': 'true', # important
            'Access-Control-Allow-Headers': 'Authorization, prefix' # important
        }
        super().__init__(request)

    async def get(self):
        prefix = self.request.headers['prefix']
        users = await db_provider.user.get_by_prefix(prefix)
        print(users)
        logins = [user.login for user in users]
        print(logins)

        return web.json_response( data=logins, headers=self.OPTIONS, status=200)
        # return [{'logins': logins}, 200]
            

    async def options(self):
        print('Something')
        return web.Response(headers=self.OPTIONS, status=200)
    
    

    

