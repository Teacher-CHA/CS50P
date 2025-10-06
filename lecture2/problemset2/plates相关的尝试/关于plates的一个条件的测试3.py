def is_alphaanddigit(y):#检验字符串里的每个元素是否是字母或数字
    for letter in y:
        if not letter.isalpha() and not letter.isdigit():
            return False#遍历每个元素，如果有不对的就false
    return True#这里不用else true是因为如果用了，那么就跳过了之后的循环就不符合我们检查每一个元素的情况了。也不能用continue，不然也会跳过。
if is_alphaanddigit(input("input:")):
    print("True")
else:
    print("false")