with open("students0.csv","r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = f"{name} is in {house}"
        students.append(student)
