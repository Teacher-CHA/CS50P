"""
使用 return value以及def编程一个猜数游戏
"""
def get_guess():
    guess = int(input("enter a guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")

main()