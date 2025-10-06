"""
从一个记录了学生姓名和所属学院的文件中读取数据，然后将每个学生的信息以 "[学生姓名] is in [学生学院]" 格式展示出来。
具体来说，要求如下：
数据来源: 有一个名为 students0.csv 的文件，里面存储了学生的姓名和学院信息，每行一条记录，姓名和学院之间用逗号分隔。
信息展示: 程序需要逐行读取 students0.csv 文件中的内容，提取出学生的姓名和学院，然后按照指定格式展示出来。
最终用户希望看到的是，程序运行后，会将所有学生的信息，按照 "[学生姓名] is in [学生学院]" 的格式按照姓名的排序输出到屏幕上,此排序的实现需要使用匿名函数lambda。
该程序需要把含有学生信息的dict放到list里面去
"""

students = []
with open("students0.csv","r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["house"]}")