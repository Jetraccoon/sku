from aiohttp import web

from api.routers import setup_routes
from api.services import parse_csv

sku_list = parse_csv()


async def create_app():
    app = web.Application()
    setup_routes(app)
    return app
