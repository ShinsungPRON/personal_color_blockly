import asyncio
import subprocess
from websockets.server import serve

async def echo(websocket):
    subprocess.run(['python3.10', '/Users/flyahn06/code/PRON/personal_color/main.py'])

async def main():
    async with serve(echo, "localhost", 8080):
        await asyncio.Future()  # run forever

asyncio.run(main())