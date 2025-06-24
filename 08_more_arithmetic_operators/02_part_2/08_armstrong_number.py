#reads a three digit number and check if the number is Armstrong number

number = int(input())

number_string = str(number)

first_digit = int(number_string[0])
second_digit = int(number_string[1])
third_digit = int(number_string[2])

sum_of_cubes = first_digit**3 + second_digit**3 + third_digit**3
is_armstrong_number = sum_of_cubes == number

print(is_armstrong_number)                                  
