#define the function that convert emoticon to emoji
def convert(text):
    """
    Args: text : input 这里参数是“text”,指的是input

    Returns: the strings which have been converted返回值是已经转变过的字符串

    这里注意的是不要让function担任过于重的任务，比如input replace 再 print，这里这个function仅承担convert就好
    """
    result = text.replace(":)","🙂").replace(":(","🙁")
    return result

def main():
    text = input("Please enter the text here ")
    result = convert(text)
    print(result)

#下面这行是说，只有再运行本程序faces_1.py时，才运行main。如果是其他程序引用该文件，则不执行main
if __name__ == "__main__":
    main()