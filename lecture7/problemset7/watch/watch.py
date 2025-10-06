"""
implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, 
and returns its shorter, shareable youtu.be equivalent as a str. 
Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. 
And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
"""
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'iframe.*src="https?://(?:www\.)?youtube\.com/embed/(?P<URL>.\w+)"'#这里iframe也是需要的，check最后一条就是看iframe存在与否的情况
    if match := re.search(pattern, s):
        URL = match.group("URL")
        return f"https://youtu.be/{URL}"
    else:
        return None

if __name__ == "__main__":
    main()