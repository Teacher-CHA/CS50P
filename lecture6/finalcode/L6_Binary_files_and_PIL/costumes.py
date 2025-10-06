"""
具体需求如下：

图片来源: 用户通过命令行参数指定一系列的图片文件。

图片读取: 程序需要读取用户指定的所有图片。

GIF 合成: 将读取到的所有图片合成为一个 GIF 动画。GIF 动画的播放顺序应该按照用户在命令行中指定的图片顺序。

GIF 参数:

动画的每一帧持续时间为 200 毫秒。

动画循环播放。

GIF 文件名: 生成的 GIF 文件名为 "costumes.gif"。

简单来说，这个工具接收一系列图片作为输入，然后把它们合并成一个循环播放的 GIF 动画，并保存为 "costumes.gif"。 需要注意的是图片的读取顺序和循环播放。
"""

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)