from aiohttp import web, web_ws


from .models import user

class ResponseBusted(web.Response):
    def __init__(self, text, status):
        super().__init__(text=text, status=status,
                         headers={'Access-Control-Allow-Origin': 'http://localhost:3000'})

def j_response(data, status = 200):
    print(data)
    return web.json_response(data={"data": "test"},
                                headers={'Access-Control-Allow-Origin': 'http://localhost:3000'})


class AuthView(web.View):
    async def get(self):
        ss = {"data": "test"}
        
        return j_response(data = ss)

