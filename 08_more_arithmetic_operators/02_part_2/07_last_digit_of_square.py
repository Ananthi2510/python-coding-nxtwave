#reads a number N and checks if the last digit of N is equal to the last digit of the square of N.

number = int(input())

square = number ** 2

number = str(number)
number_length = len(number)

square = str(square)
square_length = len(square)

number_last_digit = number[number_length - 1]
square_last_digit = square[square_length - 1]

is_last_digit_equal = (number_last_digit == square_last_digit)

if is_last_digit_equal:
    print("Equal")
else:
    print("Not Equal")
