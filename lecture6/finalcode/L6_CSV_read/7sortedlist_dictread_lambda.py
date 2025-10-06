"""
数据源：假设我们有一个名为 students.csv 的文件，文件以逗号分隔，包含学生的姓名和居住地两列信息。
数据读取：你的脚本需要读取 students.csv 文件中的数据，并将每一行数据转换为一个字典。请务必使用 DictReader 来读取文件。
数据存储：将所有学生的信息（姓名和居住地）存储在一个列表中。
数据排序：按照学生的姓名对列表中的学生姓名进行排序。请务必使用 lambda 表达式来实现排序。
数据展示：最后，你的脚本需要遍历排序后的学生信息列表，并按照 "[学生姓名] is in [学生居住地]" 的格式，输出每个学生的信息。
这里和notes不一样是因为在lecture上有学生指出了这里可以简化，而David接受了这一点。
"""

import csv

students = []

with open("students1.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["home"]}")