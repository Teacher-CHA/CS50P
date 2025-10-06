#define the function that convert emoticon to emoji
def convert():
    text = input("Please enter the text here ")
    result = text.replace(":)","🙂").replace(":(","🙁")
    print(result)

def main():
    convert()

main()