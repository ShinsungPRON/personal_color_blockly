import asyncio
import subprocess
from websockets.server import serve
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "conf.conf"))


async def echo(websocket):
    subprocess.run([config['DEFAULT']['py'], config['DEFAULT']['filepath']])


async def main():
    async with serve(echo, "localhost", 8080):
        await asyncio.Future()  # run forever

asyncio.run(main())
