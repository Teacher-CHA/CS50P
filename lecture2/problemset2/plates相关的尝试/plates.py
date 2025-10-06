def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (2 <= len(s) <= 6#条件2,这里条件2提前了是因为在submit结果中发现input：H会使得条件1中的s[1]报错，于是先说条件2以避免条件1报错
        and s[0].isalpha() and s[1].isalpha()#条件1
        and is_lastdigit(s)#条件3
        and is_firstzero(s)#条件3*
        and is_alphaanddigit(s)):#条件4
        return True
    else:
        return False

def is_lastdigit(x):#此函数为检验是否数字后还有字母
    hasbeenmetdigit = False
    for letter in x:
        if letter.isdigit():
            hasbeenmetdigit = True
#continue 的含义：跳过当前循环的剩余部分，立即开始下一次循环迭代。这里万万不能用continue
        if hasbeenmetdigit == True and letter.isalpha():
            return False
    return True

def is_firstzero(x):#此函数检验第一个数字是否是0
    for letter in x:
        if letter.isdigit():
            if letter == "0":
                return False
            else:
                return True
    return True#如果所有字符都不是数字，则return true
            
def is_alphaanddigit(y):#检验字符串里的每个元素是否是字母或数字
    for letter in y:
        if not letter.isalpha() and not letter.isdigit():
            return False#遍历每个元素，如果有不对的就false
    return True#这里不用else 

main()