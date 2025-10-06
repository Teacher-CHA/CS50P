"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, 
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; 
AAA22A would not be acceptable. The first number used cannot be a ‘0’.”这一条可以翻译成如果出现数字，数字必须出现在字母之后
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
Assume that any letters in the user’s input will be uppercase. Structure your program per the below, 
wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

isalpha() 方法

作用： isalpha() 方法用于检查字符串是否只包含字母字符。
语法：
string.isalpha()
Use code with caution.
Python
返回值：
如果字符串中所有字符都是字母字符（包括大小写字母），则返回 True。
如果字符串为空或包含非字母字符（例如，数字、空格、标点符号等），则返回 False。"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    list_letter = list(s)
    if (not list_letter[0].isalpha() or not list_letter[1].isalpha()#条件1：如果第一个或者第二个不是字母则return false
        or len(s) < 2 or len(s) > 6#条件2：如果长度不符合，则return false
        or not is_lastdigit(list_letter)#条件3：数字必须出现在字母之后否则false
        or not is_alphaanddigit(list_letter)):#条件4：如果有不是字母或数字的情况，则false
        return False
    else:
        return True
    
def is_lastdigit(x):#该函数为检验是否存在先出现数字再出现字母的情况
    hasbeenmetdigit = False#表示遇到数字了吗：没有
    for letter in x:#这条语句是按照顺序进行的，对于x的每一个字母，开始检验。根据条件1，开始的两个字符一定是字母，不满足两个if，于是省略。
        if letter.digit():
            hasbeenmetdigit = True#当遇到了digit把hasbeendigit改成了true
#只有遇到了数字并且之后的字符是字母才会触发下边这一条。举个例子：对于A1A，for遍历每个字符，先经过了A，无事发生。再经过1，这时候hasbeendigit变成了true，下面这个if不满足后者。
#最后经过A，同时满足了下面这一条，终于return false了。
        if hasbeenmetdigit and letter.isalpha():
                return False
    
def is_alphaanddigit(y):
    for letter in y:
        if letter.isalpha() or letter.digit():
            return True
        else:
            return False

main()