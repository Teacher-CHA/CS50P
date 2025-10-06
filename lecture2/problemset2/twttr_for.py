word = input("Input: ")
for letter in "aeiouAEIOU":
    word = word.replace(letter,"")
print(f"Output: {word}")