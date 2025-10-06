import re



def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)
    flag = 0
    if match:
        for i in range(1, 5):#作用是创建一个从 1 开始（包含 1），到 5 结束（不包含 5）的整数序列
            if 0 <= int(match.group(i)) <= 255:
                flag += 1
        if flag == 4:
            return True
    return False


if __name__ == "__main__":
    main()