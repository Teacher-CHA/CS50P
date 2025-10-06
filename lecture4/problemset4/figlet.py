"""
In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, 
and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, 
the program should exit via sys.exit with an error message.
"""

import random
import sys
from pyfiglet import Figlet


#下面在这行代码的作用有：调用 Figlet 类： Figlet() 是对 pyfiglet 库中 Figlet 类的一个 调用 (call) 或 实例化 (instantiation)。
#创建一个 Figlet 对象： Figlet() 会创建一个 Figlet 类的 实例 (instance)，也就是一个具体的 Figlet 对象 (object)。
#将 Figlet 对象赋值给变量 figlet： 创建的 Figlet 对象会被赋值给变量 figlet。
figlet = Figlet()
#get a list of available fonts with code，于是list_fonts目前就被赋值成了一个list
list_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    actual_font = random.choice(list_fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in list_fonts:
        actual_font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

#设置字体
figlet.setFont(font = actual_font)

#输入文本
text = input("Input: ")
print(figlet.renderText(text))