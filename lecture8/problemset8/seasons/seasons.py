"""
In a file called seasons.py, implement a program that 
prompts the user for their date of birth in YYYY-MM-DD format 
and then prints how old they are in minutes, 
rounded to the nearest integer, using English words instead of numerals, 
just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, 
assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. 
In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. 
Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today."""

from datetime import date
import inflect
import sys
import re

class Time:

    def __init__(self, birth):#这里参数仅有birth，minutes可以通过today-birth计算，不写
        self.birth = date.fromisoformat(birth)
        

    @classmethod
    def get(cls):#此class method为得到生日并检验是否正确格式，并返回cls（birth）
        try:#看看能不能改property
            birth = input("Date of Birth: ")
            pattern = r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$"
            if matches := re.search(pattern,birth):
                if (int(matches.group("year")) > 2025 or 
                    int(matches.group("month")) <1 or int(matches.group("month")) > 12 or 
                    int(matches.group("day")) <1 or int(matches.group("day")) > 31):
                        sys.exit("Invalid date")
                else:
                    return cls(birth)
            else:
                sys.exit("Invalid date")
        except ValueError:
            sys.exit("Invalid date")

    def calculate(self):#这是一个实例方法
        return (date.today() - self.birth).days * 24 * 60


def main():
    birth = Time.get()#birth是实例变量，birth有一个attribute叫做birth.birth，值为input的value
    minutes = Time.calculate(birth)
    p = inflect.engine()
    print(
        f"{p.number_to_words(minutes, andword='').capitalize()} {p.plural('minute', minutes)}"
    )

if __name__ == "__main__":
    main()