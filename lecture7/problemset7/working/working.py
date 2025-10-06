"""
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below 
and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) 
and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM

Raise a ValueError instead if the input to convert is not in either of those formats 
or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). 
But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
"""
import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    #该正则表达式大致分为4部分，to前后各两部分完全相同。第一部分就是数字部分（可能带冒号），第二部分则是时间段
    pattern = r"^(?P<first_number>\d{1,2}(\:\d{1,2})?) (?P<first_daytime>(AM|PM)) to (?P<second_number>\d{1,2}(\:\d{1,2})?) (?P<second_daytime>(AM|PM))"
    if match := re.search(pattern,s):
    #下面是把group里的内容提取出来方便后续操作，这里面可以用groups简化，但是可能没那么好找bug。
        first_number = match.group("first_number").strip()#这个可能是9:00也有可能是9
        second_number = match.group("second_number").strip()
        first_daytime = match.group("first_daytime").strip()
        second_daytime = match.group("second_daytime").strip()
    #下面就用到新定义的函数了，不然的话这个convert函数太复杂了
        start = convert_time(first_number,first_daytime)
        end = convert_time(second_number,second_daytime)
        return f"{start} to {end}"
    else:
        raise ValueError
    

def convert_time(number,daytime):#此函数输入12小时制数字（可能是9:00也有可能是9）和时间段，输出24小时制数字
    if ":" in number:#如果有冒号就分开，如果没冒号说明这是整点
        hour, minute = map(int, number.split(":"))
    else:
        hour = int(number)
        minute = 0

    if hour < 0 or hour > 12 or minute < 0 or minute >= 60:#这保证了小时和分钟的取值范围
        raise ValueError
    #下面就是根据cs50中给的表格进行的换算
    if daytime == "AM" and hour == 12:
        hour = hour - 12
    if daytime == "PM" and hour != 12:
        hour = hour + 12
    return(f"{hour:02d}:{minute:02d}")

if __name__ == "__main__":
    main()