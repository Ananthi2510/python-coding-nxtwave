first_number = int(input())
second_number = int(input())

first_number_square = first_number ** 2
second_number_square = second_number ** 2

sum_of_squares = first_number_square + second_number_square

if sum_of_squares >= 60:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")
