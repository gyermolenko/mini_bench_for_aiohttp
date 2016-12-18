from lxml import html


URLS = [
    'https://python.org',
    'https://github.com',
    'https://stackoverflow.com/',
    'https://twitter.com',
]


def parse(page):
    tree = html.fromstring(page.decode('utf-8'))
    title = tree.xpath('.//title')[0].text
    return title


def printout(results):
    for res in results:
        title = parse(res)
        print(title)
