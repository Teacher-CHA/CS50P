def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    num_dollars = round(float(d.replace("$","")),1) #remove the symbol $ ,round to one decimal place and change the type of string
    return num_dollars


def percent_to_float(p):
    num_percent = round(float(p.replace("%",""))*0.01,2) #remove the symbol % ,round to two decimal place and change the type of string
    return num_percent


main()