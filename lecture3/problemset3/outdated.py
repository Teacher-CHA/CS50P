"""In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, 
in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below.
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. 
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
提示：月份转换为数字依靠list.index
print(months.index("March"))     # 输出: 2
"""
months_text = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
  while True:
    date = input("Date: ").strip()#确保用户不会错误的输入空格，在check50里面有个input错误的输入了whitespace导致了报错
    try:
        month, day, year = date.split("/")
        test_date(month, day, year)
        printdate(month, day, year)
        break
    except ValueError:
        try:
            month_text_and_day, year = date.split(", ")
            month_text, day = month_text_and_day.split(" ")
            month = int(months_text.index(month_text)) + 1
            test_date(month, day, year)
            printdate(month, day, year)
            break
        except ValueError:
            pass
#上面是一个try-exception嵌套结构，含义是：如果A执行错误那就换B执行...
#后来我了解到这里也可以不这么写，可以通过if是否含有“/”或if len分开后的str来代替这个玩意，这样的话就不必把month的赋值写于main中了

def printdate(month, day, year):#此函数目的是填充并print年月日
  if len(str(month)) == 1:
    month = "0" + str(month)
  if len(str(day)) == 1:
    day = "0" + str(day)
  if len(str(year)) == 1:
    year = "000" + str(year)
  elif len(str(year)) == 2:
    year = "00" + str(year)
  elif len(str(year)) == 3:
    year = "0" + str(year)#后来才知道zfill方法可以补零，比较elegant
  print(f"{year}-{month}-{day}")

def test_date(month, day, year):#此函数的目的是检验年月日是否是整数，是否符合常理
  if 1 <= int(month) <=12 and 1 <= int(day) <= 31 and 0 <= int(year) <= 9999:
    pass
  else:
    raise ValueError
  
main()
