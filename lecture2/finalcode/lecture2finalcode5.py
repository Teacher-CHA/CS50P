"""已知的是
Hermione: House: Gryffindor, Patronus: Otter
Harry: House: Gryffindor, Patronus: Stag
Ron: House: Gryffindor, Patronus: Jack Russell terrier
Draco: House: Slytherin, Patronus: None (according to this example)
使用dictionary输出这四个学生的姓名,学院,守护神。如果有信息缺失，请使用Unknown"""

list_students = [
    {"name":"Hermione", "House":"Gryffindor", "Patronus":"Otter"},
    {"name":"Harry", "House":"Gryffindor", "Patronus":"Stag"},
    {"name":"Ron", "House":"Gryffindor", "Patronus":"Jack Russell terrier"},
    {"name":"Draco", "House":"Slytherin"}
]#这是一个list，每个元素都是一个dict
for dict in list_students:
    print(dict.get("name","Unknown"),dict.get("House","Unknown"),dict.get("Patronus","Unknown"),sep=", ")