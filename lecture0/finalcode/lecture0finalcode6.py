"""
该代码为定义阶乘函数并计算，使用到了递归recursion
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
def main():
    n = int(input("What's n? "))
    result = factorial(n)
    print(f"the factorial of n is {result}")

main()