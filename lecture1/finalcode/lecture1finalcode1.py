"""
比较xy大小的并使用else
注意点：1、不要忘记int函数.2、if else elif后面的冒号colon不要忘
"""
x = int(input("x= "))
y = int(input("y= "))

if x > y:
    print("x is great than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")