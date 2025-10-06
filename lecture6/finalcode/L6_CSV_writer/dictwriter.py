"""
需要实现以下功能：

收集信息： 提示用户输入学生的姓名和居住地。

数据存储： 将用户输入的学生姓名和居住地信息，以追加的方式，保存到 students.csv 文件中。如果文件不存在，则创建该文件。

数据格式： 文件应为 CSV 格式，包含 "name" 和 "home" 两列。

请务必使用 DictWriter 来写入文件。
"""
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students3.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name, "home":home})