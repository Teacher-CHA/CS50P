"""
题目：
给定一个包含字典的列表 items，每个字典代表一个商品，包含 "name"（商品名）和 "price"（价格）两个键。

items = [
    {"name": "Apple", "price": 1.0},
    {"name": "Banana", "price": 0.5},
    {"name": "Orange", "price": 0.75},
    {"name": "Grapes", "price": 2.0}
]

请编写一个Python函数 sort_by_price(items)，该函数接受 items 列表作为输入，并返回一个新的列表，其中商品按照价格从低到高排序。
要求：
使用 sorted() 函数和 key 参数来实现排序。
定义一个辅助函数来提取商品的价格。
"""

items = [
    {"name": "Apple", "price": 1.0},
    {"name": "Banana", "price": 0.5},
    {"name": "Orange", "price": 0.75},
    {"name": "Grapes", "price": 2.0}
]

def get_price(item):
    return item["price"]

for item in sorted(items,key=get_price):
    print(item)