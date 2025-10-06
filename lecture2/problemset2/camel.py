"""Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. 
For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user’s input will indeed be in camel case.
本题的要点有两个：第一、查找大写字符；第二、插入下划线

isupper()，它可以帮助我们判断一个字符是否为大写字母。
char.isupper()：如果字符 char 是大写字母，则返回 True，否则返回 False。
示例：
print("A".isupper())  # 输出: True
如何处理字符串中的多个字符？
如果你想检查一个字符串中的多个字符，你需要遍历这个字符串，并对每个字符分别使用 isupper() 方法。
例如：
text = "HelloWorld"

for char in text:

.join() 方法 (针对列表)：
.join() 方法用于将列表中的所有字符串连接成一个字符串。
string_list = ["hello", "world", "how", "are", "you"]
result = ",".join(string_list) # result 现在是 "hello,world,how,are,you"""

camelCase = input("camelCase: ")
list = list(camelCase)
newlist = ["_" + letter  if letter.isupper() else letter for letter in list]#采用了comprehension：对于list里的字母，如果大写了，则把这个字母前面加上_，否则输出原样
snake_case = "".join(newlist).lower()
print(f"snake_case: {snake_case}")

