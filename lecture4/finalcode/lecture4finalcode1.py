"""
这个程序需要实现以下功能：
需要知道你的名字： 程序运行时，需要在命令行提供一个参数，这个参数就是你的名字。

不多不少的名字：
如果运行程序时没有提供名字（缺少参数），程序要报错，提示 "Too few arguments"，然后结束。
如果运行程序时提供了多于一个名字（过多参数），程序也要报错，提示 "Too many arguments"，然后结束。

正式的问候： 如果程序运行时只提供了一个名字，程序应该打印 "hello, my name is [你的名字]"，其中 [你的名字] 是你在命令行提供的名字。
"""
import sys

if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too many arguments")

print(f"hello, my name is {sys.argv[1]}")