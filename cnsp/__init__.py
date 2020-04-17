import json
from urllib.request import urlopen
from urllib.parse import urlencode


def google(q):
    'https://www.google.cn/complete/search'
    f = urlopen(
        'https://www.google.cn/complete/search'
        f"?{urlencode({'q': q, 'client': 'psy-ab'})}"
    )
    return [
        p[0] for p in json.loads(
            f.read().decode(f.headers.get_content_charset())
        )[1]
    ]
