import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
from aiohttp import web


async def index(request):
    return web.Response(text="Welcome home!")


def main():
    app = web.Application()
    app.router.add_get('/', index)
    web.run_app(app)


if __name__ == "__main__":
    main()
