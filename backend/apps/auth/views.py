from aiohttp import web

from .models import user


class AuthView(web.View):
    async def get(self):
        print(self)
        json = {"data": "test"}
        return web.json_response(json)
