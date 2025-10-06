"""
具体的需求如下：
Account 类:
每个 Account 对象都应该有一个私有的 balance 属性，初始值为 0。 这个属性用于存储账户的余额。
需要提供一个公开的只读属性 balance，用于获取账户余额，但是不允许直接修改。

存款功能:
Account 类需要提供一个 deposit 方法，允许用户存入一定金额。 存入金额后，balance 属性应该相应增加。
取款功能:
Account 类需要提供一个 withdraw 方法，允许用户取出一定金额。 取出金额后，balance 属性应该相应减少。

测试用例:
创建一个 Account 对象。
打印账户的初始余额。
存入 100 元。
取出 50 元。
再次打印账户的余额。
输出格式:
清晰地展示账户的余额信息。 具体使用哪种方式展示余额信息由你决定。
总的来说，你需要创建一个 Account 类，提供存款、取款和查看余额的功能，并且确保余额属性的安全性。 最终，你需要展示账户的整个交易过程和最终余额。
"""
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

account = Account()
print(account.balance)
account.deposit(100)
print(account.balance)
account.withdraw(50)
print(account.balance)
