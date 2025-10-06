"""
获取邮箱地址: 提示用户输入一个邮箱地址。

验证邮箱地址: 判断用户输入的邮箱地址是否合法， 合法性通过正则表达式判断，符合以下规则：
必须包含 @ 符号
@ 符号前至少有一个字符
@ 符号后，必须有 .edu 结尾，或者有 xxx.xxx.edu结尾，xxx代表任意字符
忽略大小写

输出验证结果: 如果邮箱地址合法，输出 "Valid"； 否则，输出 "Invalid"。
"""

import re

email = input("What's your email? ").strip()
pattern = r"^\w+@(\w+\.)?\w+\.edu$"
if re.search(pattern, email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")