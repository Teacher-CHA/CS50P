"""
reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, 
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.
"""
def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    list_word = list(word)
    new_list = ["" if letter in ["a","e","i","o","u","A","E","I","O","U"] else letter for letter in list_word]
    return "".join(new_list)


if __name__ == "__main__":
    main()