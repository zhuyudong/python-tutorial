#!/usr/bin/env python3

"""Download flags of top 20 countries by population

ThreadPoolExecutor version

Sample run::

    $ PYTHONPATH=. python flags_examples/flags_threadpool.py
    DE FR BD CN EG RU IN TR VN ID JP BR NG MX PK ET PH CD US IR
    20 downloads in 0.35s

"""

from concurrent import futures

from flags_examples.flags import get_flag, main, save_flag


def download_one(cc: str):
    image = get_flag(cc)
    save_flag(image, f"{cc}.gif")
    print(cc, end=" ", flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))


if __name__ == "__main__":
    main(download_many)
