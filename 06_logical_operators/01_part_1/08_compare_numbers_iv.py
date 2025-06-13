#Reads two numbers
first_number = int(input())
second_number = int(input())

#checks if one of A and B is less than 60 and one of A and B is greater than 80.
is_less_than = (first_number < 60) or (second_number < 60)
is_greater_than = (first_number > 80) or (second_number > 80)

result = is_less_than and is_greater_than

print(result)
