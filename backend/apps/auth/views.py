from aiohttp import web

from .models import user

# async def index(request):
#     # async with request.app['db'].acquire() as conn:
#     #     cursor = await conn.execute(user.select())
#     #     records = await cursor.fetchall()
#     return web.Response(text="sdasdaslk;d apws;kd", status=200)

class AuthView(web.View):
    async def get(self):
        print(self)
        json = {"data": "test"}
        return web.json_response(json)
        # return  web.Response(text="sdasdaslk;d apws;kd")