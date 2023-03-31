from aiohttp import web, WSMsgType
import json
from database_work import db_provider
from apps.logics import headers, href


def check_chat_existing(request, ws, chat_id):
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


# Для каждого юзера есть inbox scope, куда приходят сообщения от разные юзеров, групп каналов
async def websocket_chat(request):

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
                        request.app._state[my_username] = ws  # {'Andrew': }

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


class ChatPagination(web.View):
    async def get(self):
        first_id = int(self.request.query.get('first_id'))
        second_id = int(self.request.query.get('second_id'))
        start = int(self.request.query.get('start'))

        resp = await db_provider.chat.add_chat(user1_id=first_id, user2_id=second_id)

        messages = await db_provider.chat.get_chat_messages(table_name=resp['chat_name'], start=start)

        next_href = href.create_href(
            first_id=first_id, second_id=second_id, start=start)

        data = {
            'next_href': next_href,
            'messages': messages
        }

        return web.json_response(data=data, headers=headers.GET)

    async def options(self):
        return web.Response(headers=headers.MESSAGE_OPTIONS, status=200)
