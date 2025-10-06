"""
首先，热情地欢迎玩家来到Spelling Bee！ 并友好地告知本次游戏中可使用的字母有：A、I、P、C、R、H、G。
接下来，玩家会面临几个待拼写的单词，每个单词都对应着一定的分数：
pair (4分)
hair (4分)
chair (5分)
graphic (7分)
游戏的目标是，玩家需要猜测出这些单词。
游戏进行时，请务必清晰地告诉玩家还剩下几个单词没有猜出。 玩家每猜对一个单词，就从题库中移除，并获得该单词对应的分数，并友善地告知玩家获得了多少分。
如果玩家能够直接猜出"graphic"这个单词，那么恭喜他/她，直接赢得游戏！ 并输出"You've Won!"。
"""

words = {"pair": 4, "hair": 4, "chair": 5, "graphic": 7}
letters = ["A", "I", "P", "C", "R", "H", "G"]

print("Welcome to Spelling Bee")
print(f"Your letters are: {letters}")


while True:
    word = input("Please enter your guess here: ").strip().lower()
    if word == "graphic" or len(words) == 0:
              print("You've Won!")
              break
    elif word in words.keys():
              print(f"{word} :{words[word]}")
              words.pop(word)
              print(f"There are {len(words)} left.")
    else:
              print("Please enter the valid spelling")
