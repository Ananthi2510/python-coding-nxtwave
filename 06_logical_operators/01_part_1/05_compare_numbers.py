#Reads two numbers
first_number = int(input())
second_number = int(input())

#Checks if both numbers are greater than 35 
are_greater_than = (first_number > 35) and (second_number > 35)

#Checks if first_number is greater than second_number
is_first_number_greater = first_number > second_number


#Check if both numbers are greater than 35 or first_number is greater than second_number
result = (are_greater_than) or (is_first_number_greater)

print(result)
