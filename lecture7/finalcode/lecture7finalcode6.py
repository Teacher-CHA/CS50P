"""
具体需求如下：
电话号码格式：国际电话号码由国家代码、一个空格以及后续号码组成。 
例如，一个有效的电话号码可能是 "+1 555-123-4567"，其中 "+1" 是国家代码， "555-123-4567" 是后续号码。 工具需要支持不同国家代码长度的电话号码。
国家代码识别：工具需要能够从电话号码中提取出国家代码。
归属地查询：
根据提取出的国家代码，查询预先定义好的国家代码与归属地之间的对应关系。
只有当提取出的国家代码存在于预定义的国家代码列表中时，才输出对应的归属地。

结果输出：
如果成功找到电话号码的归属地，则输出归属地名称。
如果提取出的国家代码不合法（即，不存在于预定义的国家代码列表中），则输出"Invalid"。
如果未能成功提取国家代码，则什么都不发生。

数据来源：国家代码与归属地的对应关系需要硬编码在程序中。 目前已知的信息有： "+1" 对应 "United States and Canada"，"+62" 对应 "Indonesia"， "+505" 对应 "Nicaragua"。
"""

import re

locations = {"+1": "United States and Canada","+62": "Indonesia", "+505": "Nicaragua"}

number = input("Number: ").strip()
pattern = r"^(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}$"
if match := re.search(pattern, number):
    country = locations[match.group("country_code")]
    print(country)
else:
    print("Invalid")