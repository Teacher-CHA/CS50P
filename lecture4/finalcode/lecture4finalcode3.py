"""
这个工具很简单，主要就是根据用户提供的关键词，去 iTunes 上搜索歌曲，然后把搜索结果的歌曲名字打印出来。

我们需要这样：

用户得告诉我们想搜啥，这个信息通过命令行参数传进来。如果用户没给参数，或者给的参数不对，程序直接退出，啥也别做。

连接 iTunes : 使用iTunes API。API的URL是："https://itunes.apple.com/search?entity=song&limit=50&term=" + 用户输入的关键词

把提取出来的歌名一个一个打印出来。

"""
import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
response_json = response.json()
results = response_json["results"]
for result in results:
    print(result["trackName"])