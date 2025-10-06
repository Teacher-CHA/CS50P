"""
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
    上面是航天器和离地球的距离（单位是AU），请输出航天器离地球多远
    """
dict_spaceship={
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}
for spaceship in dict_spaceship:
    print(f"{spaceship} is {dict_spaceship[spaceship]} AU from Earth")