"""
这个小工具可以通过命令行参数，从 iTunes 搜索歌曲，并以漂亮的 JSON 格式输出结果。

具体的需求是这样：
准备工作： 确保程序能够使用 json, requests, 和 sys 这三个库。

参数检查：
程序启动时，需要检查用户是否在命令行中提供了歌曲名称作为参数。
如果没有提供，或者提供的参数数量不对，程序需要直接退出，不执行任何搜索。

歌曲搜索：
使用用户提供的歌曲名称，构造一个 iTunes API 的搜索 URL。
URL 格式如下： "https://itunes.apple.com/search?entity=song&limit=1&term=" + [乐队名称]， 其中 [乐队名称] 需要替换为用户在命令行中提供的参数。

结果输出：
从 iTunes API 获取搜索结果，并将结果以缩进为2的 JSON 格式打印到控制台，要清晰易读。
"""
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
#.json()的作用是从Response 对象中提取 JSON 数据
#json.dumps的作用是格式化json数据 indent作用是缩进2