"""
使用match语句
如果输入 Harry，会输出 Gryffindor。
如果输入 Hermione，会输出 Gryffindor。
如果输入 Ron，会输出 Gryffindor。
如果输入 Draco，会输出 Slytherin。
如果输入 Alice，会输出 Who?。

注意点：
1、在match的case里面使用的是| instead of “or”
2、注意和if一样的是记得加冒号colon，这样下一行才会缩进
"""

name = input("Please enter the name here: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")