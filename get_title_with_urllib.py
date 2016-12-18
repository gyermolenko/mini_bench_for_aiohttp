from utils import URLS, parse, printout
from time import perf_counter

import urllib.request


def fetch(url):
    with urllib.request.urlopen(url) as response:
        page = response.read()
    return page


def main():
    results = []

    for url in URLS:
        page = fetch(url)
        results.append(page)

    printout(results)


if __name__ == "__main__":
    t0 = perf_counter()
    main()
    print(perf_counter() - t0)
