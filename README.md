# cnsp
[![Build Status](https://www.travis-ci.org/wangxinhe2006/cnsp.svg)](https://www.travis-ci.org/wangxinhe2006/cnsp)
[![Python Version](https://img.shields.io/pypi/pyversions/cnsp.svg)](https://www.python.org/downloads/)
[![GitHub pre-release](https://img.shields.io/github/release-pre/wangxinhe2006/cnsp.svg)](https://github.com/wangxinhe2006/cnsp/releases)
[![PyPI](https://img.shields.io/pypi/v/cnsp.svg)](https://pypi.org/project/cnsp/#history)
[![Wheel](https://img.shields.io/pypi/wheel/cnsp.svg)](https://pypi.org/project/cnsp/#files)
[![License](https://img.shields.io/github/license/wangxinhe2006/cnsp.svg)](LICENSE)

Search predictions in mainland China

## Installation
```sh
pip install cnsp
```

## Usage
```python
>>> from cnsp import google, baidu
>>> google('Google')
['google', 'google play', 'google翻译', 'google translate', 'google scholar', 'google map', 'google drive', 'google earth', 'google voice', 'google play下载']
>>> baidu('baidu')
['百度翻译', '百度', '百度识图', '百度地图', '百度网盘', 'baidu.com', '百度翻译在线翻译', '百度贴吧', '百度网盘破解版开发者', '百度推荐为什么关不了']
>>>
```
For more search engines, see [§Supported search engines](#supported-search-engines).

## Supported search engines
Function | Search engine | URL | API URL
-------- | ------------- | --- | ----------
`baidu` | 百度一下，你就知道 | [www.baidu.com](https://www.baidu.com/) | `https://www.baidu.com/sugrec`
`sm` | 神马搜索 | [m.sm.cn](https://m.sm.cn/) | `https://sugs.m.sm.cn/web`
`sogou` | 搜狗搜索引擎 - 上网从搜狗开始 | [www.sogou.com](https://www.sogou.com/) | `https://www.sogou.com/suggnew/ajajjson`
`so` | 360搜索，SO靠谱 | [www.so.com](https://www.so.com/) | `https://sug.so.360.cn/suggest`
`google` | Google | [www.google.cn](https://www.google.cn/) | `https://www.google.cn/complete/search`
`yam` | yam蕃薯藤-搜尋 | [search.yam.com](https://search.yam.com/) | `https://search.yam.com/Search/Mobile/GetRelatedKeywords.aspx`
