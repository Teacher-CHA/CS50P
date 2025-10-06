 #让user输入数字来确定meow几次，如果不是正整数，则不发生.并使用while true语法
def main():
    number = int(input("What's n? "))
    meow(get_number(number))

def get_number(n):
    while True:
        if n > 0:
            return n

def meow(m):
    for _ in range(m):
        print("moew")

main()