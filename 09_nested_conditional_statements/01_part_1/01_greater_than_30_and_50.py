#reads a number X and checks if it is greater than 30 and 50

number  = int(input())

is_number_greater_than_30 = number > 30
is_number_greater_than_50 = number > 50

if is_number_greater_than_30:
    print("X is Greater than 30")

    if is_number_greater_than_50:
        print("X is Greater than 50")
