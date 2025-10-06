"""
Food 类:
每个 Food 对象都有一个 hearts 属性，表示它的治疗量。
Food 有一个默认的基础治疗量（base_hearts），base_hearts 的初始值设定为 1。 这个值可以在后续被调整。
Food 接受一个 ingredients 列表作为参数。
Food 根据 ingredients 来计算 hearts 值。 规则是：
首先，hearts 等于 base_hearts。
然后，遍历 ingredients 列表。如果某个 ingredient 的名字里包含了 "hearty"（忽略大小写），则 hearts 增加 2 点；否则，增加 1 点。

特殊食物：
我们需要一种特殊的方法，可以直接创建一个 Food 对象，并且指定它的 hearts 值，而不需要提供 ingredients。 也就是说，这是一个只有hearts数值但没有成分的食物。

测试用例：
创建一个包含 "Mushroom" 和 "Hearty Mushroom" 的食物，展示它的治疗量。
改变 Food 的 base_hearts 值，然后再次创建一个包含 "Mushroom" 和 "Hearty Mushroom" 的食物，展示它的治疗量。
使用特殊方法创建一个治疗量为 2 的食物，展示它的治疗量。

输出格式：
使用合适的字符串格式化方法输出食物的治疗量。 格式是："This [食物名称] heals [治疗量] hearts! ❤️" （具体使用哪种字符串格式化方法由你决定）。
"""
class Food:
    base_hearts = 1#这是class variable属于范围更广的变量（比起instance variable）
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
    
    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    @classmethod
    def from_nothing(cls, hearts):
        Food = cls(ingredients=[])
        Food.hearts = hearts
        return Food
    
def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This Mushroom Skewer heals {mushroom_skewer.hearts} hearts! ❤️")

    Food.base_hearts = 2
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This Mushroom Skewer heals {mushroom_skewer.hearts} hearts! ❤️")

    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This Mushroom Skewer heals {mushroom_skewer.hearts} hearts! ❤️")


main()