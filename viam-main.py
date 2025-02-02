# my-python-robot/main.py

import asyncio
from viam.rpc.server import Server

from my_cool_arm import MyCoolArm

async def main():
    srv = Server([MyCoolArm('my-arm')])
    await srv.serve()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        pass