"""
具体需求如下：
获取输入: 提示用户输入他们的邮箱地址。
验证邮箱: 验证用户输入的邮箱地址是否符合教育机构邮箱的格式。具体来说，我们希望验证邮箱地址满足以下条件：
以 .edu 结尾。
包含且仅包含一个 @ 符号。
@ 符号前后都有内容。

输出结果:
如果邮箱地址是有效的教育机构邮箱，输出 "Valid"。
如果邮箱地址不是有效的教育机构邮箱，输出 "Invalid"。
"""

import re

email = input("What's your email? ").strip()
pattern = r"^[^@]+@[^@]+\.edu$"
if re.search(pattern, email):
    print("Valid")
else:
    print("Invalid")