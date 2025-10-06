word = input("Input: ")
list_word = list(word)#把word每个字母都变成list里的元素（这一步和camel里面一样）
newlist = ["" if letter in "aeiouAEIOU" else letter for letter in list_word]#对于list_word里的字母，如果在aeiou里面的就replace成虚无，否则保持原样
newword = "".join(newlist)
print(f"Outpput: {newword}")