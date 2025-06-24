#Reads a number
#Checks if the number is divisible by 3
#print triple of the number if it is divisible , otherwise print the double of the number 
number = int(input())

if (number % 3 == 0):
  print(number * 3)
else: 
  print(number * 2)
  
