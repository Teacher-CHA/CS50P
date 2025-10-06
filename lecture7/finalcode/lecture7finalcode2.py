"""
询问邮箱: 首先，要友好的询问用户，"What's your email?" 并获取用户输入的邮箱地址。
检查邮箱格式: 判断用户输入的邮箱地址是否合法。 合法的邮箱地址需要满足以下条件：
用户名部分： 只能包含字母、数字、下划线。

域名部分： 至少包含一个 . 符号，并且以 .com, .edu, .gov, .net 或者 .org 结尾。

给出结论:
如果邮箱地址符合格式，输出 "Valid"。
否则，输出 "Invalid"。
"""

import re

email = input("What's your email? ").strip()
pattern = r"^\w+@\w+\.(com|edu|gov|net|org)$"
if re.search(pattern, email):
    print("Valid")
else:
    print("Invalid")