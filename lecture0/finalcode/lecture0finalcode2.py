"""
该代码为格式化输出x+y的值,并四舍五入保留一位小数
输出x/y的值,并四舍五入保留2位小数
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x+y,1)
p = x/y

print(f"x+y={z:,}")
print(f"x/y={p:.2f}")