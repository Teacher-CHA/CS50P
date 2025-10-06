"""
这个工具的功能是，将英语姓名从书写习惯调整为口语习惯，但仅当输入符合特定格式时才进行调整和输出。
获取姓名： 询问用户 "What's your name?" 并获取用户的输入。 我们期望用户输入的是符合英语书写习惯的姓名，也就是 "LastName, FirstName" 的形式 (例如: Smith, John)。
格式校验： 程序需要验证用户输入是否符合 "LastName, FirstName" 的格式。 如果不符合，则不进行任何操作，直接结束。
姓名调整（仅当格式正确时）： 如果输入符合格式，程序需要将用户的姓名调整为英语口语习惯的 "FirstName LastName" 形式 (例如: John Smith)。
此外，如果在last、firstname之间不存在或存在多个空格也需要正确处理。
打招呼（仅当格式正确时）： 如果输入符合格式，最后，程序需要向用户打招呼，输出 "Hello, [调整后的名字]"。

关键点：
程序必须首先验证输入格式。 只有当用户输入的名字符合 "LastName, FirstName" 的格式时，才进行后续的调整和输出操作。
如果输入格式不正确，程序不应该输出任何内容。
重点在于使用正则表达式提取名字的部分，并进行重新组合。"""

import re

name = input("What's your name? ").strip()
pattern = r"^(.+), *(.+)$"
if match := re.search(pattern, name):
    print(f"Hello, {match.group(2)} {match.group(1)}")