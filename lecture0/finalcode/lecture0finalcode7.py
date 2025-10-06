"""
该代码为先创建一个全局变量再通过函数内部修改这个变量
"""

emoticon = "v.v"

def say(phrase):
    print(f"{phrase} {emoticon}")

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi")

main()