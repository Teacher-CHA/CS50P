"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
output how many cents in change the user is owed. Assume that the user will only input integers, 
and ignore any integer that isn’t an accepted denomination.
"""

amountdue = 50
while amountdue > 0:
    print(f"Amount Due: {amountdue}")#先告诉用户还需要多少钱
    insertcoin = int((input("Insert coin: ")))#让用户放钱进来
    if insertcoin == 25 or insertcoin == 10 or insertcoin == 5:
     amountdue = amountdue - insertcoin#只有以上几个数才能生效
    else:
       continue#其他数字的话就不鸟它，直接重复
else:
   changeowed = -amountdue
   print(f"Change owed: {changeowed}")
