"""
我们需要开发一个魔法世界银行系统。这个系统的目标是帮助魔法师们管理他们的财产，具体来说，就是 Galleons, Sickles, 和 Knuts。
系统需要实现以下功能：
创建 Vault： 每个魔法师可以创建一个属于自己的 Vault，并在创建时设定初始的 Galleons, Sickles, 和 Knuts 数量。如果不设定，默认都是 0。
展示 Vault： 魔法师可以随时查看自己 Vault 里的财产情况，系统需要以清晰易读的格式展示 Galleons, Sickles, 和 Knuts 的数量。展示格式请参考以下输出示例。
合并 Vault： 魔法师之间可以合并 Vault。**请务必使用运算符重载（Operator Overloading）来实现 Vault 的合并功能。
**也就是说，你需要定义一个特殊的方法，使得可以使用 + 运算符直接合并两个 Vault 对象。
当两个 Vault 对象使用 + 运算符进行操作时，系统应该自动将两个 Vault 中的 Galleons, Sickles, 和 Knuts 数量分别相加，创建一个新的 Vault，并返回这个新的 Vault 对象。

现在，假设有以下两位魔法师：
魔法师 Potter，他的 Vault 里有 100 Galleons, 50 Sickles, 和 25 Knuts。
魔法师 Weasley，他的 Vault 里有 25 Galleons, 50 Sickles, 和 100 Knuts。

请你编写这个程序，帮助他们管理自己的财富。
你的程序需要：
分别创建 Potter 和 Weasley 的 Vault 对象。
展示 Potter 和 Weasley 的 Vault 信息。
使用运算符重载合并 Potter 和 Weasley 的 Vault 对象，并将合并后的 Vault 对象存储在一个名为 total 的变量中。
展示合并后的 Vault 信息。

输出示例：
100 Galleons, 50 Sickles, 25 Knuts
25 Galleons, 50 Sickles, 100 Knuts
125 Galleons, 100 Sickles, 125 Knuts
Use code with caution.
请确保你的代码能够正确创建 Vault、展示 Vault 信息、使用运算符重载合并 Vault，并最终按照上述示例格式展示 Potter、Weasley 以及合并后的 Vault 信息。
"""
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)