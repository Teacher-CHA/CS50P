import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input("Name: ")
        name_list.append(name.strip())
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(name_list)}")
