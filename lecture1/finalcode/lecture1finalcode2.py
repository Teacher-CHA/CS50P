"""
根据score输出output
"""
score = int(input("Please enter the score here "))

def grade(x):
    print(f"Grade: {x}!")

def main():
    if score >= 90:
        grade("A")
    elif score >= 80:
        grade("B")
    elif score >= 70:
        grade("C")
    elif score >= 60:
        grade("D")
    else:
        grade("E")

main()