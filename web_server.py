from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def home(request):
    return web.Response(text="Bot is running!")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
