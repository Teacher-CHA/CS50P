"""
通过游戏难度和游戏人数推荐游戏
难度 (Difficulty)	玩家数量 (Players)	推荐游戏
Difficult	         Multiplayer	  Poker
Difficult	         Single-player	  Klondike
Casual              Multiplayer	      Hearts
Casual	             Single-player	  Clock
其他情况提示user enter valid content
"""
def main():
    difficulty = input("Please enter the difficulty here: ")
    if difficulty != "Difficult" and difficulty != "Casual":
        print("Please enter a valid difficulty")
        exit()#这里exit()比return好是因为这里并没有在function内部，而是“main”里面，所以使用exit函数更好
    players = input("Please enter the players here: ")
    if not (players == "Multiplayer" or players == "Single-player"):#这里的（）表示先进行or的逻辑运算，而not表示对后者的逻辑全部取反，即！= and ！=
        print("Please enter a valid difficulty")
        exit()
    
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")
    
def recommend(game):
    print(f"You might like {game}")

main()