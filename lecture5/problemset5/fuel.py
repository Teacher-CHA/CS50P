"""
convert expects a str in X/Y format as input, wherein each of X and Y is an integer, 
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. 
If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""

def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))

def convert(fraction):
    while True:
        x,y = fraction.split(sep="/")
        if int(x) > int(y) or int(x) < 0 or int(y) < 0:
            raise ValueError
        if int(y) == 0:
            raise ZeroDivisionError
        z = int(x) / int(y) * 100
        return int(f"{z:.0f}")

    

def gauge(percentage):
    if not isinstance(percentage, int):
        raise ValueError("The percentage is not an integer.")
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()