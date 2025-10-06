"""In a file called grocery.py, implement a program that prompts the user for items,
 one per line,
 1、 until the user inputs control-d (which is a common way of ending one’s input to a program). 
 2、Then output the user’s grocery list in all uppercase, 
 3、sorted alphabetically by item, 
 4、prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
 Treat the user’s input case-insensitively."""

dict = {}
while True:
    try:
       item = input("").upper()
       if not item in dict:
         dict[item] = 1
       else:
          dict[item] = dict[item] + 1
       sorteddict = sorted(dict.keys())
    except EOFError:
        break

for x, y in sorted(dict.items()):
          print(f"{y} {x}")
#for x in sorteddict:
#          print(f"{dict[x]} {x}")
#这条代码死活通不过check，改成上面这个代码就能通过，但我觉得没有区别啊。