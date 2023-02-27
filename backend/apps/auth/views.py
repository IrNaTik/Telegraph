from aiohttp import web
import json

async def index(request):
    
    data = { "message": "Hello world"}
    
    return web.Response(text=json.dumps(data), status=200)