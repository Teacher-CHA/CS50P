"""
该代码为输出hello＋用户first name
"""

#ask for user's name
name = input("What's your name? ")

#capitalize the first letter of every word and remove the whitespace
name = name.strip().title()

#split the first name and last name
first, last=name.split(" ")

#say hello to user
print(f"hello, {first}")
