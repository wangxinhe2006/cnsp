import json
import re
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen

__version__ = '0.0.3'


def baidu(q):
    'https://www.baidu.com/sugrec'
    f = urlopen(
        'https://www.baidu.com/sugrec'
        f"?{urlencode({'json': '1', 'prod': 'pc', 'wd': q})}"
    )
    try:
        return [
            p['q']
            for p in json.loads(
                f.read().decode(f.headers.get_content_charset())
            )['g'] if p['type'] == 'sug'
        ]
    except KeyError:
        return []


def sm(q):
    'https://sugs.m.sm.cn/web'
    f = urlopen(
        'https://sugs.m.sm.cn/web'
        f"?{urlencode({'q': q})}"
    )
    return [
        p['w'] for p in json.loads(
            f.read().decode(f.headers.get_content_charset())
        )['r']
    ]


def sogou(q):
    'https://www.sogou.com/suggnew/ajajjson'
    f = urlopen(
        'https://www.sogou.com/suggnew/ajajjson'
        f"?{urlencode({'key': q, 'type': 'web'})}"
    )
    try:
        return json.loads(
            '[%s]' % re.fullmatch(
                r'window\.sogou\.sug\((.+)\);',
                f.read().decode(f.headers.get_content_charset())
            ).group(1)
        )[0][1]
    except HTTPError:
        return []


def so(q):
    'https://sug.so.360.cn/suggest'
    f = urlopen(
        'https://sug.so.360.cn/suggest'
        f"?{urlencode({'format': 'json', 'word': q})}"
    )
    return [
        p['word'] for p in json.loads(
            f.read().decode(f.headers.get_content_charset())
        )['result']
    ]


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


def yam(q):
    'https://search.yam.com/Search/Mobile/GetRelatedKeywords.aspx'
    f = urlopen(
        'https://search.yam.com/Search/Mobile/GetRelatedKeywords.aspx'
        f"?{urlencode({'k': q})}"
    )
    return re.findall(
        r'<lable>(.+?)</lable>',
        f.read().decode(f.headers.get_content_charset())
    )
