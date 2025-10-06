"""
构建一个包裹运输计费系统，它的作用是计算包裹的运费，并展示包裹的信息和运费明细。
这个系统需要满足以下需求：
包裹信息记录: 能够记录包裹的编号number、发件人sender、收件人recipient以及重量weight等基本信息。
运费计算: 能够根据包裹的重量和每公斤的运费单价cost_per_kg=2，计算出包裹的总运费。
信息展示: 能够清晰地展示包裹的详细信息，包括包裹编号、发件人、收件人、重量以及最终的运费。举例: Package 1: Alice to Bob, 10 kg costs $20。

具体来说，你需要完成以下几点：
定义一个 Package 类，用于存储包裹的信息。
实现一个方法，用于根据包裹的重量和每公斤的运费单价，计算包裹的运费。
实现一个方法，能够以易于理解的格式展示包裹的详细信息（包括包裹编号、发件人、收件人、重量）。
创建一个 Package 对象，并计算其运费，然后将包裹信息和运费清晰地展示出来。
"""
class Package:
    cost_per_kg = 2
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        self.cost = Package.calculate_cost(weight)#这里我想看看能不能用class method 发现也可以,也可以使用老师讲的实例方法，可以参考note里面的笔记

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight} kg costs ${self.cost}"
    
    @classmethod
    def calculate_cost(cls, weight):
        return weight * cls.cost_per_kg
    
package = Package(1, "Alice", "Bob", 10)
print(package)