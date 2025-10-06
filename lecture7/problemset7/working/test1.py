#该文件仅仅是写代码过程中的测试，看看正则表达式对不对
import re

s = input("Hours: ").strip()

pattern = r"^(?P<first_number>\d{1,2}(\:\d{2})?) (?P<first_daytime>(AM|PM)) to (?P<second_number>\d{1,2}(\:\d{2})?) (?P<second_daytime>(AM|PM))"
match = re.search(pattern,s)
#下面是把group里的内容提取出来方便后续操作
if match:
    first_number = match.group("first_number").strip()#这个可能是9:00也有可能是9
    second_number = match.group("second_number").strip()
    first_daytime = match.group("first_daytime").strip()
    second_daytime = match.group("second_daytime").strip()
    print(first_number)