#reads a three digit number

number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

#Checks if all the digits of the number are same
result = first_digit == second_digit == third_digit 
print(result)
