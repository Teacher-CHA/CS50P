"""
我们需要你开发一个能让用户输入数字的小工具，我们叫它 get_int.py。这个工具的主要目标是让用户输入一个整数，并且在用户输入错误时给出提示。
具体来说，我们希望你的代码实现以下功能：
主流程 (main()):
调用一个名为 get_int() 的函数，让用户输入一个整数，然后将结果存入名为 x 的变量。
最后，打印出 "x is [用户输入的整数]"，其中 [用户输入的整数] 是实际用户输入的数字。
获取整数 (get_int()):
它会一直询问用户 "What's x?"，直到用户输入一个有效的整数为止。
如果用户输入的不是整数（比如输入了字母或者符号），就提示 "x is not an integer"。
如果用户输入的是整数，就把这个整数返回。
"""
def main():
    value = get_int()
    print(f"x is {value}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()
        