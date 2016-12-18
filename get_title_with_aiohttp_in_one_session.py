from utils import URLS, printout
from time import perf_counter

import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        page = await response.read()
    return page


async def run(loop):

    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(fetch(session, url)) for url in URLS]
        results = await asyncio.gather(*tasks)

    printout(results)


def main():
    loop = asyncio.get_event_loop()

    future = asyncio.ensure_future(run(loop=loop))
    loop.run_until_complete(future)

    loop.close()


if __name__ == "__main__":
    t0 = perf_counter()
    main()
    print(perf_counter() - t0)
