
from aiohttp import web, WSMsgType
import json
from datetime import datetime
from database_work import db_provider




def check_chat_existing(request, ws ,chat_id):
    if chat_id == None:
        return request
    check_websocket = request.app.get(chat_id, None)
    if check_websocket == None:
        request.app[chat_id] = []
    request.app[chat_id].append(ws)
    
    return request

async def check_user_existing(username):
    response = await db_provider.user.get_user_id_by_username(username)
    return response

        
async def websocket_chat(request): # Для каждого юзера есть inbox scope, куда приходят сообщения от разные юзеров, групп каналов 

    
    username = request.query['username']
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    print('Сокет установлен')
    
    
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            data = json.loads(msg.data)
            msg_type = data.get('type', None)
            
            if msg_type:
                if msg_type == 'chatBegin':
                    my_username = data.get('myUsername', None)
                    person_username = data.get('personUsername', None)
                    response = await check_user_existing(person_username)

                    if my_username not in request.app: 
                        request.app._state[my_username] = ws # {'Andrew': }

                    print(my_username)
                    # print(request.app._state[my_username])
                    # print(my_username in request.app._state)
                        

                    # if response['error']
                    # request = check_chat_existing(request, ws , chat_id) # Если чата с таким id не было, то будет создан
                elif msg_type == 'message':
                    message = data.get('message', None)
                    sender_username = data.get('senderUsername', None)
                    getter_username = data.get('getterUsername', None)


                    print(getter_username in request.app._state)
                    print(sender_username in request.app._state)
                    
                    print(sender_username, getter_username)
                    
                    try:
                        _ws = request.app._state[getter_username]

                        if 'eof' not in str(_ws):
                            print(_ws)
                            await _ws.send_json({'type': 'message', 'message': message, 'senderUsername': sender_username})
                        else:
                            del request.app._state[getter_username]
                    except:
                        pass

        # elif msg.type == WSMsgType.PING                
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    # Get user last visit and update the databse
    # print(datetime.utcnow())
    # user_id = await db_provider.user.get_user_id('Ignatio')
    # response = await db_provider.user.get_access_data_table()
    # print(response)
    # await db_provider.user.update_access_data_table()
    
    print('websocket connection closed', username)
    del request.app._state[username]
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
            'Access-Control-Allow-Headers': '''authorization''',
            'Access-Control-Request-Headers': '''authorization''',
            
        }
        super().__init__(request)

    async def get(self):
<<<<<<< HEAD
        # prefix = self.request.headers
        # users = await db_provider.user.get_by_prefix(prefix)
        # logins = [user.login for user in users]

        print('Goooood')
        print(self.request.query['username'], 'Good')
        username = self.request.match_info.get('username', "Anonymous")
        print(username)

        return web.json_response(data={1: 2}, headers=self.GET, status=200) 
=======
        
        print(self)
        return web.json_response(data={1,2}, headers=self.GET, status=200) 
>>>>>>> 377e2d3e21686852ea86d14c4e2cee15b00d6676
            

    async def options(self):
        print('$$$$$$$$')
        return web.Response(headers=self.OPTIONS)
    
async def get_chat_existing(request):
        if 'OPTIONS' in str(request):
                print('Options')
                return web.Response(headers= {
                        'Access-Control-Allow-Origin': 'http://localhost:3000',
                        'Access-Control-Allow-Credentials': 'true',
                        'Allow': 'OPTIONS, GET, POST',
                        'Access-Control-Request-Method': 'POST',
                        'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
                        'Access-Control-Allow-Headers': '''authorization''',
                        'Access-Control-Request-Headers': '''authorization''',
                        
                    })
            
        print(request.query['username'], 'Good')
        print(request.query['myUsername'], 'Good2')
        username1 = request.query['username']
        username2 = request.query['myUsername']
            
        resp1 = await db_provider.user.get_user_id_by_username(username1)
        resp2 = await db_provider.user.get_user_id_by_username(username2)
        print(resp1, resp2)
        if resp1['error'] == False and resp2['error'] == False:
            resp = await db_provider.chat.add_chat(resp1['user_id'], resp2['user_id'])

            if resp['error'] == False and resp['isNewChat'] == False:
                return web.json_response(data={'chatExists': True, 'usernameExists': True}, headers={'Access-Control-Allow-Origin': 'http://localhost:3000',
                                                            'Access-Control-Allow-Credentials': 'true'}, status=200) 
            else:
                return web.json_response(data={'chatExists': False, 'usernameExists': True}, headers={'Access-Control-Allow-Origin': 'http://localhost:3000',
                                                            'Access-Control-Allow-Credentials': 'true'}, status=200) 
        else:
            return web.json_response(data={'chatExists': False, 'usernameExists': False, 'optional': {'user1': resp1, 'user2': resp2}}, headers={'Access-Control-Allow-Origin': 'http://localhost:3000',
                                                            'Access-Control-Allow-Credentials': 'true'}, status=200) 


