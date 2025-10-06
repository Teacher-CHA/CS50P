"""
implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, 
if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, 
but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

275.3.6.28, which isn’t actually a valid IPv4 (or IPv6) address.
An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, 
akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. 
But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! 
If only NUMB3RS had validated the address in that scene!
"""
import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)
    if not match:
        return False
    for i in range(1, 5):#作用是创建一个从 1 开始（包含 1），到 5 结束（不包含 5）的整数序列
            if int(match.group(i)) < 0 or int(match.group(i)) > 255:
                return False
    return True


if __name__ == "__main__":
    main()