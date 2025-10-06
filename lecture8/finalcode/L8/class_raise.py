"""
这个程序模拟了霍格沃茨魔法学校的新生入学登记和守护神（patronus）召唤仪式。

程序的具体流程如下：
学生信息登记：
程序会要求用户输入学生的姓名（Name）、学院（House）和守护神（Patronus）。
学院只能是以下四个选项之一：Gryffindor（格兰芬多）, Hufflepuff（赫奇帕奇）, Ravenclaw（拉文克劳）, Slytherin（斯莱特林）。 如果用户输入的学院不在这些选项中，程序需要报错。
守护神是可选的，如果用户选择输入守护神，那么守护神只能是以下三个选项之一：Stag（牡鹿）, Otter（水獭）, Jack Russell terrier（杰克罗素梗犬）。 如果用户输入的守护神不在这些选项中，程序需要报错。
如果学生没有守护神，则守护神可以为 None。
如果学生没有姓名，程序需要报错。

守护神召唤仪式：
#添加的一点：程序会最先输出"[学生姓名] from [学生学院]"
程序会先输出 "Expecto Patronum!"（呼神护卫！）。
然后，程序会根据学生登记的守护神，显示对应的魔法效果。
如果守护神是 Stag（牡鹿），则显示 🦌 (鹿的emoji)
如果守护神是 Otter（水獭），则显示 🦦 (水獭的emoji)
如果守护神是 Jack Russell terrier（杰克罗素梗犬），则显示 🐶 (狗的emoji)
如果没有守护神，则显示 "🪄" (魔杖的emoji)

例如，如果用户输入：
Name: Harry Potter
House: Gryffindor
Patronus: Stag
程序应该输出：
Expecto Patronum!
🦌
再例如，如果用户输入：
Name: Draco Malfoy
House: Slytherin
Patronus:
程序应该输出：
Expecto Patronum!
🪄
Use code with caution.
再举个例子，如果用户输入：
Name:
House: Slytherin
Patronus:
程序应该报错： "Missing name"
"""

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus
        
    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = get_student()
    print(f"{student}\nExpecto Patronum!\n{student.charm()}")

def get_student():
    name = input("Name: ").title()
    house = input("House: ").title()
    patronus = input("Patronus: ").title()
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()