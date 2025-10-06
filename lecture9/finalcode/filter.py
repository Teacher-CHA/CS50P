"""
假设你现在是霍格沃茨的入学管理员，你需要从学生名单中找到所有属于格兰芬多学院的学生，并按名字的字母顺序展示他们。

这是现有的学生名单：
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]
Use code with caution.
Python
你的程序需要完成以下任务：
筛选格兰芬多学生： 从学生名单中筛选出所有学院为格兰芬多的学生。请务必使用 filter 函数和 lambda 表达式来实现。
排序： 将筛选出的格兰芬多学生按照名字的字母顺序进行排序。 请务必使用 lambda 表达式来实现。
展示学生姓名： 按照排序后的顺序，将所有格兰芬多学生的姓名打印出来。
"""
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for s in sorted(gryffindors,key=lambda s: s["name"]):
    print(s["name"])