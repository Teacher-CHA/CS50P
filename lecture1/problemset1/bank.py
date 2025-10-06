"""
关于startswith()的用法
string.startswith(prefix, start, end)
string：这是你想要检查的字符串。
prefix：这是一个必需的参数，它表示你想要查找的前缀字符串。
start (可选)：这是一个整数，表示从字符串的哪个位置开始搜索。默认值是 0 (字符串的开头)。
end (可选)：这是一个整数，表示到字符串的哪个位置结束搜索。默认值是字符串的末尾。
返回值：
如果字符串以指定的 prefix 开头，startswith() 方法返回 True。
否则，它返回 False。
"""

greeting = input("Greeting: ").strip().lower()
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
