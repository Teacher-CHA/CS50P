"""
角色定义： 定义三个类：Wizard（巫师）、Student（学生）和 Professor（教授）。
继承关系： Student 和 Professor 必须继承自 Wizard 类，体现他们都是巫师的本质。

属性定义：
Wizard 类应具有 name（姓名）属性。如果创建 Wizard 对象时没有提供姓名，则应抛出一个 ValueError 异常，提示 "Missing name"。
Student 类应具有 name（姓名）和 house（学院）属性。
Professor 类应具有 name（姓名）和 subject（科目）属性。

信息输出：
创建 Wizard 对象时，输出 "Wizard: [巫师姓名]"。
创建 Student 对象时，输出 "Student: [学生姓名], House: [学生学院]"。
创建 Professor 对象时，输出 "Professor: [教授姓名], Subject: [教授科目]"。
"""
class Wizard():
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        else:
            self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject