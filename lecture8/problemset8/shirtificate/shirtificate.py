from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4') # 设置方向、单位和格式
pdf.add_page()# 添加上述页面

pdf.set_font("helvetica", style="B", size=24) # 设置字体
pdf.text(67, 30, txt="CS50 Shirtificate") # 添加文本

pdf.image("shirtificate.png", x=50, y=50, w=100) # 添加图片，并设置位置和宽度

name = input("Please enter your name: ")

pdf.set_text_color(255,255,255)  # 设置文本颜色
pdf.set_font("helvetica", style="B", size=30)# 设置字体
pdf.text(88, 80, txt=name) # 添加文本
pdf.text(75, 90, txt="took CS50") # 添加文本

pdf.output("shirtificate.pdf")#输出保存