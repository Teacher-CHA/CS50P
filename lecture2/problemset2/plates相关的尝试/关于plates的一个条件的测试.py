def is_lastdigit(x):#此函数为检验是否数字后还有字母
    hasbeenmetdigit = False
    for letter in x:
        if letter.isdigit():
            hasbeenmetdigit = True
#continue 的含义：跳过当前循环的剩余部分，立即开始下一次循环迭代。这里万万不能用continue
        if hasbeenmetdigit == True and letter.isalpha():
            return False
    return True

if is_lastdigit(input("input:")):
    print("True")
else:
    print("false")