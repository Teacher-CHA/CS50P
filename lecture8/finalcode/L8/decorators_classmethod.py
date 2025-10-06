"""学生类 (Student):
需要定义一个学生类，包含姓名和学院两个属性。
姓名和学院信息在创建学生对象时通过构造函数传入。
需要有一个方法，能够以 "[姓名] from [学院]" 的形式返回学生的信息。

属性访问控制 (property, setter):
为了保证数据的有效性，需要对学生姓名和学院进行控制。
姓名字段不能为空，如果为空则抛出异常。
学院字段只能是 "Gryffindor"，“Hufflepuff”，“Ravenclaw”，“Slytherin" 四个学院之一，如果不是这四个学院，则抛出异常。

学生信息录入 (get_student):
需要实现一个在class内部的class method，用于录入学生的信息。
该函数提示用户输入学生的姓名和学院。
根据用户输入的信息创建一个学生对象。
返回创建的学生对象。

信息展示 (main):
程序的主函数调用学生信息录入函数，获取一个学生对象。
并且尝试修改学生的house
将学生对象的信息打印出来。"""

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house#就算main函数内没有新赋值self.house的内容，setter也会触发，因为在init函数中self.house被赋值了，这里也会触发setter

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        else:
            self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        else:
            self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
        
def main():
    student = Student.get()
    student.house = "Suzhou"#该行代码为测试setter是否能够运行，报错说明setter可以运行
    print(student)

if __name__ == "__main__":
    main()