"""
is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, 
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; 
AAA22A would not be acceptable. The first number used cannot be a ‘0’.”这一条可以翻译成如果出现数字，数字必须出现在字母之后
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
Assume that any letters in the user’s input will be uppercase. Structure your program per the below, 
wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if  len(s) < 2 or len(s) > 6:#条件2
        return False
    if  not s[0].isalpha() or not s[1].isalpha():#条件1
        return False


#检验是否数字后还有字母
    hasbeenmetdigit = False
    for letter in s:
        if letter.isdigit():
            hasbeenmetdigit = True
#continue 的含义：跳过当前循环的剩余部分，立即开始下一次循环迭代。这里万万不能用continue
        if hasbeenmetdigit == True and letter.isalpha():
            return False

#此函数检验第一个数字是否是0
    for letter in s:
        if letter.isdigit():
            if letter == "0":
                return False
            else:
                break
            
#检验字符串里的每个元素是否是字母或数字
    for letter in s:
        if not letter.isalpha() and not letter.isdigit():
            return False#遍历每个元素，如果有不对的就false
        
    return True#如果上面这些条件都没有return false那么就是true了


if __name__ == "__main__":
    main()