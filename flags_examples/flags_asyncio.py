#!/usr/bin/env python3

"""Download flags of top 20 countries by population

asyncio + aiottp version

Sample run::

    $ PYTHONPATH=. python flags_examples/flags_asyncio.py
    EG VN IN TR RU ID US DE CN MX JP BD NG ET FR BR PH PK CD IR
    20 flags downloaded in 1.07s
"""

import asyncio

from httpx import AsyncClient

from flags_examples.flags import BASE_URL, main, save_flag


async def download_one(client: AsyncClient, cc: str):
    image = await get_flag(client, cc)
    save_flag(image, f"{cc}.gif")
    print(cc, end=" ", flush=True)
    return cc


async def get_flag(client: AsyncClient, cc: str) -> bytes:
    url = f"{BASE_URL}/{cc}/{cc}.gif".lower()
    resp = await client.get(url, timeout=6.1, follow_redirects=True)
    return resp.read()


def download_many(cc_list: list[str]) -> int:
    return asyncio.run(supervisor(cc_list))


async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:
        to_do = [download_one(client, cc) for cc in sorted(cc_list)]
        res = await asyncio.gather(*to_do)

    return len(res)


if __name__ == "__main__":
    main(download_many)
