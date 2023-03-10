from aiohttp import web, web_ws
from ..models import Chats # Класс для работы с json данными

def j_response(data, status = 200):
    return web.json_response(data=data,
                                headers={'Access-Control-Allow-Origin': 'http://localhost:3000/chat-access/'})


class WebSocketAccessView(web.View):
    async def get(self):
        data = self.request

        return web.json_response(data={'usernameExists': 'Yes'},
                                headers={'Access-Control-Allow-Origin': 'http://localhost:3000',
                                         'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
                                         'Access-Control-Allow-Headers': 'X-PINGOTHER, Content-Type, username'})