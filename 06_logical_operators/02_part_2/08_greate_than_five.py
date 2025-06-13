#Reads two numbers
first_number = int(input())
second_number = int(input())

#check if both the numbers are positive and if atleast one of them is greater than 5
are_positive = (first_number > 0) and (second_number >0)
is_greater = (first_number > 5) or (second_number > 5)

result = are_positive and is_greater
print(result)
