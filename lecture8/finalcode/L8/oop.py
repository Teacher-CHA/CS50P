"""
使用新函数收集学生信息: 程序需要询问学生的姓名和学院意向,并返回dict.

特殊处理: 如果学生的名字是 "Padma"，那么无论她选择哪个学院，都强制将她分到 "Ravenclaw"。

展示结果: 最后，程序需要以 "[学生姓名] from [学生学院]" 的格式，显示学生被分配到的学院。
"""

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student["name"]} from {student["house"]}")

if __name__ == "__main__":
    main()