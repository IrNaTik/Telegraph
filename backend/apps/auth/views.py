from aiohttp import web, web_ws


from .models import user

class ResponseWithHeaders(web.Response):
    def __init__(self, text, status):
        super().__init__(text=text, status=status,
                         headers={'Access-Control-Allow-Origin': 'http://127.0.0.1:3000'})




class AuthView(web.View):
    async def get(self):
        print(self)
        json = {"data": "test"}
        return web.json_response(json)

async def handler(request):
    return web.Response(text="asda", status=200)