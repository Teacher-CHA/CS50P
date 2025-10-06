"""
具体需求如下：
输入 URL： 脚本需要提示用户输入一个 Twitter 的 URL。

URL 格式校验与提取：
脚本需要判断用户输入的 URL 是否是有效的 Twitter URL。
有效的 Twitter URL 应该符合以下模式：
可以以 http:// 或 https:// 开头。 https 中的 "s" 是可选的。
www. 是可选的。
必须包含 twitter.com/。
在 twitter.com/ 之后，应该紧跟着用户名。 用户名由字母、数字和下划线组成。

提取用户名： 如果 URL 是有效的 Twitter URL，则提取用户名。 
用户名应该是不包含任何其他字符的纯用户名，同时使用正则表达把不需要的group设置成不获取位置，把需要获取位置的地方进行命名“Username”。#该条要求为添加了shorts里的知识点。
输出用户名： 如果成功提取到用户名，则按照 "Username: [用户名]" 的格式，输出用户名。

例如，如果用户输入以下 URL：
https://twitter.com/elonmusk
http://twitter.com/elonmusk
https://www.twitter.com/elonmusk
http://www.twitter.com/elonmusk
那么你的脚本应该输出：
Username: elonmusk
"""
import re

url = input("URL: ").strip()
pattern = r"^https?://(?:www\.)?twitter\.com/(?P<Username>\w+)$"
if match := re.search(pattern, url, re.IGNORECASE):
    print(f"Username: {match.group("Username")}")