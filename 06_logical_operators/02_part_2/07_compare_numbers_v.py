#Reads two numbers
first_number = int(input())
second_number = int(input())

#check if one of the given numbers is negative and product of the numbers is greater than or equal to -46.
is_negative = (first_number < 0) or (second_number < 0)
is_product_greater = (first_number * second_number) >= -46

result = is_negative and is_product_greater
print(result)
