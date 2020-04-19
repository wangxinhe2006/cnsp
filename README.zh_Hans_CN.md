# cnsp
[![Build Status](https://www.travis-ci.org/wangxinhe2006/cnsp.svg)](https://www.travis-ci.org/wangxinhe2006/cnsp)
[![Python 版本](https://img.shields.io/pypi/pyversions/cnsp.svg)](https://www.python.org/downloads/)
[![GitHub pre-release](https://img.shields.io/github/release-pre/wangxinhe2006/cnsp.svg)](https://github.com/wangxinhe2006/cnsp/releases)
[![PyPI](https://img.shields.io/pypi/v/cnsp.svg)](https://pypi.org/project/cnsp/#history)
[![Wheel](https://img.shields.io/pypi/wheel/cnsp.svg)](https://pypi.org/project/cnsp/#files)
[![License](https://img.shields.io/github/license/wangxinhe2006/cnsp.svg)](LICENSE)

🎌 [English](README.md) | **大陆简体**

中国大陆可用的搜索联想

## 安装
```sh
pip install cnsp
```

## 使用方法
```python
>>> from cnsp import google, baidu
>>> google('Google')
['google', 'google play', 'google翻译', 'google translate', 'google scholar', 'google map', 'google drive', 'google earth', 'google voice', 'google play下载']
>>> baidu('baidu')
['百度翻译', '百度', '百度识图', '百度地图', '百度网盘', 'baidu.com', '百度翻译在线翻译', '百度贴吧', '百度网盘破解版开发者', '百度推荐为什么关不了']
>>>
```
更多搜索引擎，见 [§支持的搜索引擎](#支持的搜索引擎)。

## 支持的搜索引擎
函数 | 搜索引擎 | URL | 请求域名
---- | -------- | --- | --------
`baidu` | 百度一下，你就知道 | https://www.baidu.com | `www.baidu.com`
`sm` | 神马搜索 | https://m.sm.cn | `sugs.m.sm.cn`
`sogou` | 搜狗搜索引擎 - 上网从搜狗开始 | https://www.sogou.com | `www.sogou.com`
`so` | 360搜索，SO靠谱 | https://www.so.com | `sug.so.360.cn`
`google` | Google | https://www.google.com.hk | `www.google.cn`
`yam` | yam蕃薯藤-搜尋 | https://search.yam.com | `search.yam.com`
