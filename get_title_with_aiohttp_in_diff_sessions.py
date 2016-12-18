from utils import URLS, printout
from time import perf_counter

import asyncio
import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            page = await response.read()
    return page


def main():
    loop = asyncio.get_event_loop()

    tasks = [loop.create_task(fetch(url)) for url in URLS]

    results = loop.run_until_complete(asyncio.gather(*tasks))
    printout(results)

    loop.close()


if __name__ == "__main__":
    t0 = perf_counter()
    main()
    print(perf_counter() - t0)
