""""
In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, 
saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, 
resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, 
using default values for method, bleed, 
and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, 
and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos, 
so that, when they’re resized and cropped, the shirt appears to fit perfectly.
"""

import sys
from PIL import Image, ImageOps


if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid input")
elif not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid input")
_, type1 = sys.argv[1].rsplit(".")
_, type2 = sys.argv[2].rsplit(".")
if type1 != type2:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as im:
        im = ImageOps.fit(im, shirt.size)
#这行代码使用 ImageOps.fit() 函数来调整用户图像 im 的大小，使其适应 shirt.size 的大小。
#ImageOps.fit() 函数会裁剪并缩放输入图像，以完全填充指定的尺寸，并保持图像的宽高比。
#shirt.size 是一个元组，包含 shirt 图像的宽度和高度 (例如: (width, height))。

        im.paste(shirt, shirt)
#这行代码使用 paste() 方法将 shirt 图像粘贴到 im 图像上。
#第一个 shirt 参数是要粘贴的图像（即 shirt.png）。
#第二个 shirt 参数是要粘贴的位置。 更准确地说是要粘贴的区域。 这里使用 shirt 图像本身作为 mask 和 box 参数. 这意味着 shirt 图像将会被粘贴到 im 图像的 shirt 图像所占据的区域。
#但是这实际上会将 shirt 完整地覆盖到 im 上，因为 shirt 的大小已经被调整到和 im 相同。

        im.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File does not exist.")
