# aiohttpdemo_polls/main.py
import asyncio

from aiohttp import web
import aiohttp_jinja2
import jinja2

from routes import setup_routes
from settings import config, BASE_DIR
from db import pg_context
from middlewares import setup_middlewares


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR/'aiohttpdemo_polls'/'templates')))
setup_routes(app)
setup_middlewares(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app, port=443)
