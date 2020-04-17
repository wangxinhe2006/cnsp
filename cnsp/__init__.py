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


def baidu(q):
    'https://www.baidu.com/sugrec'
    res = urlopen(
        'https://www.baidu.com/sugrec'
        f"?{urlencode({'json': '1', 'prod': 'pc', 'wd': q})}"
    )
    try:
        return [
            s['q']
            for s in json.loads(
                res.read().decode(res.headers.get_content_charset())
            )['g'] if s['type'] == 'sug'
        ]
    except KeyError:
        return []
