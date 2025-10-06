"""对lecture3finalcode2.py使用raise exceptions"""

def main():
    value = get_int()
    print(f"x is {value}")

def get_int():
    while True:
        x = input("What's x? ")
        if x.isdigit():
            return int(x)
        else:
            raise ValueError("x is not an integer")

main()