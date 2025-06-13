#Reads two numbers
first_number = int(input())
second_number = int(input())

sum = first_number + second_number

is_negative = (first_number < 0) or (second_number < 0)
is_greater_than = sum > 7

#checks if one of the given numbers is a negative number and the sum of the given numbers is greater than 7.
result = is_negative and is_greater_than

print(result)
