"""
该代码为定义hello函数，并向user say hello
"""

def hello(to="world"):
    print(f"hello,{to}")

def main():
    name = input("What's your name? ")
    name = name.strip().title()
    hello(name)
    hello()

main()
