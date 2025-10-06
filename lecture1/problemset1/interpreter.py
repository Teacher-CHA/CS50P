"""
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and 
outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

string.split(sep=None, maxsplit=-1)
string: 要进行拆分的字符串。
sep (可选): 指定用于拆分字符串的分隔符。
如果 sep 没有指定或为 None（默认值），split() 会使用任何空格（包括空格、制表符、换行符等）作为分隔符。
如果 sep 指定了一个字符串，split() 会使用该字符串作为分隔符进行拆分。
maxsplit (可选): 指定最多拆分的次数。
如果 maxsplit 为负数或未指定（默认值 -1），split() 会拆分所有出现的 sep 分隔符。
如果 maxsplit 为正数，split() 只会进行 maxsplit 次拆分，剩余部分将作为最后一个元素保留在列表中。

返回值:
split() 方法返回一个字符串列表，其中包含了根据分隔符拆分后的子字符串。
"""
expression = input("Expression: ").strip()
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
   a = x + z
   print(f"{a:.1f}")
elif y == "-":
   b = x - z
   print(f"{b:.1f}")
elif y == "*":
   c = x * z
   print(f"{c:.1f}")
elif y == "/":
   if z == 0:
      print("Please enter the valid arithmetic expression")
   else:
      d = x / z
      print(f"{d:.1f}")
else:
   print("Please enter the valid arithmetic expression")
