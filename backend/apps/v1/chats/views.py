
from aiohttp import web, WSMsgType
import json
from database_work import db_provider


def check_chat_existing(request, ws ,chat_id):
    if chat_id == None:
        return request
    check_websocket = request.app.get(chat_id, None)
    if check_websocket == None:
        request.app[chat_id] = []
    request.app[chat_id].append(ws)
    
    return request
        
async def websocket_chat(request): # request это что-то по типу scope

    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            data = json.loads(msg.data)
            msg_type = data.get('type', None)
            
            if msg_type:

                if msg_type == 'chatId':
                    chat_id = data.get('chatId', None)
                    request = check_chat_existing(request, ws , chat_id) # Если чата с таким id не было, то будет создан
                elif msg_type == 'message':
                    message = data.get('message', None)
                    chat_id = data.get('chatId', None)

                    for _ws in request.app[chat_id]:
                        if 'eof' not in str(_ws):
                            await _ws.send_json({'type': 'message', 'message': message, 'chatId': chat_id})

        # elif msg.type == WSMsgType.PING                
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws


class GetChatWithUser(web.View):
    def __init__(self,request) -> None:
        
        self.GET = {'Access-Control-Allow-Origin': 'http://localhost:3000',
                    'Access-Control-Allow-Credentials': 'true'}
        self.POST = {
            
                    }
        self.OPTIONS = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Credentials': 'true',
            'Allow': 'OPTIONS, GET, POST',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
            'Access-Control-Allow-Headers': '''*''',
            'Access-Control-Request-Headers': '''*''',
            
        }
        super().__init__(request)

    async def get(self):
        prefix = self.request.headers
        # users = await db_provider.user.get_by_prefix(prefix)
        # logins = [user.login for user in users]

        return web.json_response(data={1: 2}, headers=self.GET, status=200) 
            

    async def options(self):
        return web.Response(headers=self.OPTIONS)
