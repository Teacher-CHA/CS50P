#采用list输出 排名、姓名demo:1、Hermione 2、Harry 3、Draco
students = ["Hermione", "Harry", "Draco"]
for i in range(len(students)):#for i in 一定是range（数字），一定不要忘了range
    print(f"{i+1}、{students[i]}",end=" ")