"""
具体需求如下：

数据来源：程序需要读取一个名为 views.csv 的 CSV 文件，该文件包含图像的 id，英文标题和日文标题。

亮度分析：对于 views.csv 文件中的每一行数据，程序需要根据图像的 id，找到对应的图像文件 (例如，如果 id 是 123，那么对应的图像文件就是 123.jpeg)。 然后，程序需要分析该图像文件的亮度。

结果写入：程序需要创建一个新的 CSV 文件，名为 analysis.csv。 新的文件需要在原有的 id，英文标题和日文标题的基础上，增加一列 "brightness"，用于存储图像的亮度信息。

数据格式：analysis.csv 文件需要包含以下几列：id, english_title, japanese_title, brightness。 brightness 列的值需要保留两位小数。

请注意，程序需要能够处理 views.csv 文件中的每一行数据，计算对应图像的亮度，并将结果写入 analysis.csv 文件中。同时，程序需要能够正确处理图像文件不存在的情况"""
import csv
import numpy as np
from PIL import Image


def main(): 
    with open("views.csv","r", encoding="utf-8") as views, open ("analysis.csv","w", encoding="utf-8") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:#此时row已经是dict了
           brightness = calculate_brightness(f"{row["id"]}.jpeg")
           writer.writerow({"id":row["id"], "english_title":row["english_title"], "japanese_title":row["japanese_title"],"brightness":round(brightness,2)})
           

def calculate_brightness(filename):#该函数被定义为计算亮度，题目已给出
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()