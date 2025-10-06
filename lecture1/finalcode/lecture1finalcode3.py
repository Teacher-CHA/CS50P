"""
奇偶检验函数
"""
x = int(input("Please enter a integer here "))

def main():
    if is_even(x):
        print("the integer is EVEN!")
    else:
        print("the integer is ODD!")

def is_even(n):
    return n % 2 == 0
"""
这里一行代码被称作pythonic
当然也可以用传统方法
def is_even(n)
    if n % 2 == 0:
       return True
    else:
       return False
"""

main()