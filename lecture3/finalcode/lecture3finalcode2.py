"""
获取数字的工具 (get_int):
这个工具要不停地问用户：“What's x?”，直到用户输入一个整数为止。
如果用户输入的东西不是整数，比如输入了“abc”或者“1.23”，那就忽略这次输入，继续问。
如果用户输入的是一个整数，那就把这个整数拿走，交给需要它的人。
这个过程可能要一直重复，直到拿到一个整数。

展示结果:
当main拿到get_int给的整数后，就得把它展示出来，告诉用户：“x is [用户输入的整数]”。
注意，这里的[用户输入的整数]必须是实际用户输入的数字哦。"""

def main():
    value = get_int()
    print(f"x is {value}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            pass
        else:
            return x

main()