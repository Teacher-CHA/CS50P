"""
嘿！ 我们现在需要你做一个简单的抽卡模拟器。

卡池里有三张卡片： "jack", "queen", "king"。

但是，这可不是一个公平的卡池！ "jack" 这张卡出现的概率非常高，而 "queen" 和 "king" 几乎不可能出现。

我们需要你实现的功能是： 从这个卡池中随机抽取两张卡片，并展示给用户。 由于卡池的特殊设定，用户几乎总是能抽到 "jack"。
"""
import random

cards = ["jack", "queen", "king"]
random_cards = random.choice(cards, weights=[100, 0, 0], k = 2)
print(random_cards)