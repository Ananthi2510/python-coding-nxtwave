#Reads two numbers
first_number = int(input())
second_number = int(input())

are_positive = (first_number > 0) and (second_number > 0)
are_less_than = (first_number < 70) and (second_number < 70)

#checks if both A and B are positive numbers or both A and B are less than 70.
result = are_positive or are_less_than

print(result)
