"""已知的是
#Hermione: House: Gryffindor, Patronus: Otter
Harry: House: Gryffindor, Patronus: Stag
Ron: House: Gryffindor, Patronus: Jack Russell terrier
Draco: House: Slytherin, Patronus: None (according to this example)
使用dictionary输出这四个学生的姓名，学院"""
name_house={
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
}

for name in name_house:
    print(f"{name}, {name_house[name]}")