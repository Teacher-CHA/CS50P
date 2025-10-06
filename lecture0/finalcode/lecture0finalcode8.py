"""
该代码为将含有大小写混用、短语前后有多余空格的一大串字符生成表格
"""

SHOWS = [
" Avatar: the last airbender",
"Ben 10"
"Arthur",
" Spongebob Squarepants",
"Phineas and ferb",
"Kim possible",
"Jimmy Neutron ",
"the Proud family"
]

def main():
    clean_shows = []
    for show in SHOWS:
        show = show.strip().title()
        clean_shows.append(show)
    print(','.join(clean_shows))


main()
