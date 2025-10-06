"""
此代码为定义平方函数并计算,并使用return value
"""

def square(n):
    return n**2

def main():
    n=int(input("n= "))
    x=square(n)
    print(f"x squared is {x}")
main()