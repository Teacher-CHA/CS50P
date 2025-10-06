"""该代码为通过定义函数以及for loops输出3*3的hash块"""
#先定义打印一行x个#并换行
def line(x):
    for _ in range(x):
        print("#",end="")
    print()
#再定义要打印多少行
def square(y):
    for _ in range(y):
        line(y)

square(3)