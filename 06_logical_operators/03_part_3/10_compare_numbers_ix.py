#Reads a three digit number
number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

#checks if any of the below conditions is satisfied.
#Each digit of the given number is greater than 7.
#The product of any two digits is always less than or equal to 30.

is_greater = (first_digit > 7) and (second_digit > 7) and (third_digit > 7)

is_first_second_product_lesser = (first_digit * second_digit) <= 30
is_second_third_product_lesser = (second_digit * third_digit) <= 30
is_third_first_product_lesser = (third_digit * first_digit) <= 30

is_product_lesser = is_first_second_product_lesser and is_second_third_product_lesser and is_third_first_product_lesser

result = is_greater or is_product_lesser
print(result)
