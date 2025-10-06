"""你的程序需要完成以下任务：
1.  **卡牌数据源:** 准备一个名为 `hearthstone_cards.csv` 的 CSV 文件，其中包含卡牌的名称 (`name`) 和稀有度 (`rarity`) 两列数据。
2.  **卡牌数据读取与校验:** 编写函数从 `hearthstone_cards.csv` 文件中读取卡牌数据。
    *   卡牌名称需要校验，确保只包含字母、数字和空格。
    *   卡牌稀有度需要校验，确保是 "Common", "Rare", "Epic", "Legendary" 中的一个。
    *   对于不符合校验规则的卡牌数据，请在控制台输出错误信息，并跳过该卡牌的后续处理。
3.  **用户交互界面:**
    *   程序启动后，应显示一个主菜单，包含以下选项：
        *   "1. View All Cards"
        *   "2. Search for Card"
        *   "3. Exit"
    *   根据用户选择，执行相应的操作。
4.  **查看所有卡牌:** 如果用户选择 "View All Cards"，程序应将所有卡牌的名称和稀有度信息，以清晰的格式输出到控制台。
5.  **卡牌搜索:** 如果用户选择 "Search for Card"，程序应提示用户输入搜索关键词。
    *   用户可以输入卡牌名称或稀有度进行搜索。
    *   程序应在卡牌数据中搜索包含关键词的卡牌，并将匹配的卡牌信息输出到控制台。
    *   如果没有找到任何匹配的卡牌，则输出提示信息。
6.  **数据存储:** 卡牌数据应存储在适当的数据结构中，以便于后续的搜索和展示。
7.  **程序退出:** 如果用户选择 "Exit"，程序应结束运行。

请注意，程序需要具备良好的错误处理机制，并能够处理用户输入的各种情况。 例如，文件不存在，输入不合法，搜索不到结果等。
此外，需要你尽量使用函数，实现代码的模块化。  并添加适当的类型提示（Type Hints）使代码更易阅读。
"""

import csv
import re

def validate_card_name(name):
    if not re.match(r"^[a-zA-Z0-9\s]+$", name):
        raise ValueError("Error: Invalid card name format.")
    return name

def validate_rarity(rarity):
    valid_rarities = ["Common", "Rare", "Epic", "Legendary"]
    if rarity not in valid_rarities:
        raise ValueError("Error: Invalid card rarity.")
    return rarity

def get_card_data(csv_file):
    cards = []
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    name = validate_card_name(row['name'])
                    rarity = validate_rarity(row['rarity'])
                    card = {"name": name, "rarity": rarity}
                    cards.append(card)
                except ValueError:
                    print("Error: Invalid card.")
        return cards
    except FileNotFoundError:
        print("Error: The file was not found.")
        pass


def display_card_info(card):
    print(f"Card Name: {card['name']}, Rarity: {card['rarity']}")

def search_card(cards, search_term):
    results = [card for card in cards if search_term.lower() in card['name'].lower() or search_term.lower() in card['rarity'].lower()]
    if results:
        print("Search Results:")
        for card in results:
            display_card_info(card)
    else:
        print("Error: The card was not found.")

def main():
    csv_file = "hearthstone_cards.csv"
    cards = get_card_data(csv_file)
    while True:
        print("\nHearthstone Card Database")
        print("1. View All Cards")
        print("2. Search for Card")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAll Cards:")
            for card in cards:
                display_card_info(card)
        elif choice == "2":
            search_term = input("Enter card name or rarity to search for: ")
            search_card(cards, search_term)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()