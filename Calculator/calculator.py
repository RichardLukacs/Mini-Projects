TVA = 19/100
number_1 = float(input("Give a number: "))

while True:
    option = int(input("""
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Raise to a power
    6.Integral Part
    7.Remainder
    8.TVA (TVA value and price without TVA)
    9.Degrees Celsius in Fahrenheit
    10.Degrees Fahrenheit in Celsius
    11.Reset
    12.Exit
    
    """))

    if option == 1:
        number_2 = float(input("Give another number: "))
        number_1 = number_1 + number_2
    elif option == 2:
        number_2 = float(input("Give another number: "))
        number_1 = number_1 - number_2
    elif option == 3:
        number_2 = float(input("Give another number: "))
        number_1 = number_1 * number_2
    elif option == 4:
        number_2 = float(input("Give another number: "))
        while number_2 == 0:
            number_2 = float(input("Value cannot be 0. Give another number: "))
        number_1 = number_1 / number_2
    elif option == 5:
        number_2 = float(input("Give another number: "))
        number_1 = number_1 ** number_2
    elif option == 6:
        number_2 = float(input("Give another number: "))
        number_1 = number_1 // number_2
    elif option == 7:
        number_2 = float(input("Give another number: "))
        number_1 = number_1 % number_2
    elif option == 8:
        tva_from_number = TVA * number_1
        price_without_tva = number_1 - tva_from_number
        print(f'TVA is {tva_from_number} and the price without TVA is {price_without_tva}')
    elif option == 9:
        temp_f = (number_1 * 9/5) + 32
        print(f'Temp in C is {number_1} and in F is {temp_f}')
    elif option == 10:
        temp_c = (number_1 - 32) * 5/9
        print(f'Temp in F is {number_1} and in C is {temp_c}')
    elif option == 11:
        number_1 = 0
    elif option == 12:
        break
    else:
        print('Wrong option')

    if not (option == 8 or option == 11 or option == 9):
        print(f'Current result: {number_1}')
