
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
    # await ws.send_json({'type': 'requestForChatId'})
    
        
    
    async for msg in ws:
        # print(msg)
        # print(request.app.__dir__())
        # print(ws._closed)
        
        if msg.type == WSMsgType.TEXT:
            
            data = json.loads(msg.data)

            msg_type = data.get('type', None)
            print(msg_type) 
            
            if msg_type:
                if msg_type == 'chatId':
                    chat_id = data.get('chatId', None)
                    print(chat_id)
                    request = check_chat_existing(request, ws , chat_id) # Если чата с таким id не было, то будет создан
                elif msg_type == 'message':
                    message = data.get('message', None)
                    chat_id = data.get('chatId', None)

                    print(message, chat_id)
                    print(request.app[chat_id])
                    for _ws in request.app[chat_id]:
                        if 'eof' not in str(_ws):
                            await _ws.send_json({'type': 'message', 'message': message, 'chatId': chat_id})

                        
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws


class GetChatWithUser(web.View):
    def __init__(self,request) -> None:
        
        self.GET = {'Access-Control-Allow-Origin': 'http://localhost:3000',
                    'Access-Control-Allow-Credentials': 'true',
                    'Allow': 'OPTIONS, GET, POST',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
            'Access-Control-Allow-Headers': '''Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization''',
            'Access-Control-Request-Headers': '''myUsername, otherUsername'''
        }
        self.POST = {
            
                    }
        self.OPTIONS = {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Access-Control-Allow-Credentials': 'true',
            'Allow': 'OPTIONS, GET, POST',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
            'Access-Control-Allow-Headers': '''Content-Type''',
            'Access-Control-Request-Headers': '''myUsername, otherUsername'''
        }
        super().__init__(request)

    async def get(self):
        prefix = self.request.headers
        print(prefix)
        # users = await db_provider.user.get_by_prefix(prefix)
        # logins = [user.login for user in users]

        return web.json_response(data={1: 2}, headers=self.GET, status=200) 
            

    async def options(self):
        print(11111)
        return web.Response(headers=self.OPTIONS)
