def is_firstzero(x):#此函数检验第一个数字是否是0
    for letter in x:
        if letter.isdigit():
            if letter == "0":
                return False
            else:
                return True
            break
if is_firstzero(input("input:")):
    print("True")
else:
    print("false")