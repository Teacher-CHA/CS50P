#此文件仅测试get方法的正确性

import re
import sys

try:
    birth = input("Date of Birth: ")
    pattern = r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$"
    if matches := re.search(pattern,birth):
        if (int(matches.group("year")) > 2025 or 
            int(matches.group("month")) <1 or int(matches.group("month")) > 12 or 
            int(matches.group("day")) <1 or int(matches.group("day")) > 31):
                sys.exit("Invalid date")
        else:
            print(birth)
    else:
        sys.exit("Invalid date")
except ValueError:
    sys.exit("Invalid date")