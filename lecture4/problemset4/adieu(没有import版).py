"""
In a file called adieu.py, implement a program that prompts the user for names, one per line, 
until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, 
separating two names with one and, three names with two commas and one and, and n names with n-1 commas and one and.
"""
name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        last_name = name_list.pop()
        break
if len(name_list) == 0:
    print(f"Adieu, adieu, to {last_name}")
elif len(name_list) == 1:
    print(f"Adieu, adieu, to {name_list[0]} and {last_name}")
elif len(name_list) >= 2:
    part_name = ", ".join(name_list)
    print(f"Adieu, adieu, to {part_name}, and {last_name}")