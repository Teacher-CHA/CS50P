def einstein(number):
    """
    the function convert mass to energy

    Args: number : the integer of mass which is input

    Returns: the integer of energy
    """
    number_energy = number*300000000**2
    return number_energy


def main():
    number = int(input("Please enter the number of mass in kilogram "))
    number_energy = einstein(number)
    print(f"the equivalent number of Joules is {number_energy}")

main()