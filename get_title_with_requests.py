from utils import URLS, printout
from time import perf_counter

import requests


def fetch(session, url):
    page = session.get(url)
    return page.content


def main():
    results = []

    with requests.session() as session:
        for url in URLS:
            page = fetch(session, url)
            results.append(page)

    printout(results)


if __name__ == "__main__":
    t0 = perf_counter()
    main()
    print(perf_counter() - t0)
