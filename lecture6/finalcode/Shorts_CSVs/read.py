"""
具体需求如下：

图片信息来源: 有一个名为 views.csv 的文件，该文件记录了图片的相关信息， 其中每一行都包含一个图片 ID。

图片读取: 程序需要读取 views.csv 文件中的图片 ID，并根据图片 ID 找到对应的图片文件（假设图片文件名为 "[图片 ID].jpeg"）。

亮度计算: 计算每一张图片的亮度值。 计算方法是，将图片转换为灰度图，然后计算灰度图所有像素的平均值，并将其作为图片的亮度值。#该步骤是题目给出的

亮度展示: 将每张图片的亮度值四舍五入保留两位小数后进行展示。
"""
import csv
import numpy as np
from PIL import Image


def main(): 
    with open("views.csv","r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:#此时row已经是dict了
           brightness = calculate_brightness(f"{row["id"]}.jpeg")
           print(round(brightness, 2))



def calculate_brightness(filename):#该函数被定义为计算亮度，题目已给出
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()
