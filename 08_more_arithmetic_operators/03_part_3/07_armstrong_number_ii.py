#Reads a four digit number 
#Checks if N is armstrong number 

number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])
fourth _digit = int(number[3])

is_armstrong_number = ((first_digit ** 4) + (second_digit ** 4) + (third_digit ** 4) + (fourth_digit ** 4)) == number 

if  is_armstrong_number:
  print("Armstrong Number")
else:
    print("Not an Armstrong Number")
