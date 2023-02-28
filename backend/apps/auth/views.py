from aiohttp import web, web_ws

import json

class ResponseWithHeaders(web.Response):
    def __init__(self, text, status):
        super().__init__(text=text, status=status,
                         headers={'Access-Control-Allow-Origin': 'http://127.0.0.1:3000'})



async def index(request):
    
    data = { "message": "Hello world"}

    return ResponseWithHeaders(text=json.dumps(data), status=200)
    


async def registration(request): # post
    
    try:
        print(request)
        print(type(request))
        print(request.__dict__)
        username = request.query['name']
        message = { 'message': f"Hi, { username }!" }
        return web.Response(text=json.dumps(message), status=200)
    except Exception as e:
        message = { 'message': str(e) }
        return web.Response(text=json.dumps(message), status=500)
    
async def chat(request):
    client = web_ws.WebSocketResponse
    print(client)
    client.ping(b"Hello")
    return web.Response(text=json.dumps("fdfs"), status=200)