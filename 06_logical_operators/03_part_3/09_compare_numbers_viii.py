#Reads a three digit number
number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

#checks if all the below conditions are satisfied
#The number contains 1
#The sum of all the digits of the number is less than 12
#The last digit of the number is equal to 5

is_digit_one = (first_digit == 1) or (second_digit == 1) or (third_digit == 1)

sum_of_digits = first_digit + second_digit + third_digit
is_sum_less_than = sum_of_digits < 12

is_last_digit_five = third_digit == 5

result = is_digit_one and is_sum_less_than and is_last_digit_five
print(result)
