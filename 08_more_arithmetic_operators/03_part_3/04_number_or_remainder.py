#reads a number 

number = int(input())

#Checks if one of the given conditions are satisfied
#number is divisible by 5 and number is divisible by 7 
#number is less than 7 

is_divisible_by_5_and_7 = (number % 5 == 0) and (number % 7 == 0)
is_less_than = number < 7 

#print the number if any of the given conditions is satisfied 
#otherwise print the remainder when the number is divided by 5 and when the number is divided by 7 

if (is_divisible_by_5_and_7) or (is_less_than):
  print(number)
else:
  print(number % 5)
  print(number % 7)
