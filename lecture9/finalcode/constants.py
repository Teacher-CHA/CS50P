"""
Cat 类:创建一个名为 Cat 的类。
Cat 类应该有一个类属性 MEOWS，用于定义猫叫的次数，默认值为 3。
meow 方法:
Cat 类应该有一个名为 meow 的方法。
meow 方法应该循环 MEOWS 次，每次循环都在控制台输出 "meow"。

测试用例:
创建一个 Cat 类的实例。
调用实例的 meow 方法。
"""
class Cat:
    MEOWS = 3

    def meow(self):
        print("meow\n" * Cat.MEOWS,end="")

cat = Cat()
cat.meow()