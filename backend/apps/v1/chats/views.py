
from aiohttp import web, WSMsgType
import json


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

                        
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws

