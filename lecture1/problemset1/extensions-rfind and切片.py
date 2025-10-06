"""
Q:In a file called extensions.py, implement a program that prompts the user for the name of a file 
and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

本题关键在于如何把最后一个dot的后面的内容提取出来，一开始想到之前使用的split，但是如果文件名有多个dot，该方案会有问题。我们考虑rfind
rfind() 方法的基本语法如下：

string.rfind(sub, start, end)
string：这是你想要搜索的字符串。
sub：这是你想要查找的子字符串。
start (可选)：这是一个整数，表示从字符串的哪个位置开始搜索（从右向左搜索）。默认值是字符串的末尾。
end (可选)：这是一个整数，表示到字符串的哪个位置结束搜索（从右向左搜索）。默认值是 0 (字符串的开头)。

返回值：
如果找到了子字符串 sub，rfind() 方法返回子字符串最后一次出现的 索引位置。
如果没有找到子字符串 sub，rfind() 方法返回 -1。

示例：
text = "my.document.report.txt"
print(text.rfind("."))      # 输出: 18 (最后一个 . 的索引)
print(text.rfind(".", 0, 10)) # 输出: 2 (从索引 0 到 10 中，最后一个 . 的索引)
print(text.rfind("a"))      # 输出: -1 (没有找到 "a")
print(text.rfind("."))

对比 find() 和 rfind():
find() 方法从字符串的左侧开始搜索，并返回第一次出现的索引位置。
rfind() 方法从字符串的右侧开始搜索，并返回最后一次出现的索引位置。

字符串切片 (String Slicing):
字符串切片允许你通过指定起始和结束索引来提取字符串的一部分。它的基本语法如下：

string[start:end:step]

start: 这是切片的起始索引（包含）。如果省略，则默认从字符串的开头开始。
end: 这是切片的结束索引（不包含）。如果省略，则默认到字符串的末尾结束。
step: 这是切片的步长，用于指定从 start 到 end 的移动方式。如果省略，则默认为 1，表示连续取值。
"""
name = input("File name: ").strip().lower()
position_dot = name.rfind(".")
suffix = name[position_dot +1:]

match suffix:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
