"""
作为霍格沃茨分院仪式的新手，你需要快速将几个学生的学院分配为格兰芬多。已知学生名单如下：
students = ["Hermione", "Harry", "Ron"]
你需要创建一个程序 `assign_gryffindor.py`，将花名册上的所有学生都分配到格兰芬多，然后将结果以字典的形式展示出来， 字典的键是学生姓名，值是"Gryffindor"。 
**请务必使用字典推导式完成此任务。**
"""
students = ["Hermione", "Harry", "Ron"]
dict = {student : "Gryffindor" for student in students}
print(dict)