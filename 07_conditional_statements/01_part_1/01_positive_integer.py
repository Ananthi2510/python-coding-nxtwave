#reads a number and converts it to a positive number.
number = int(input())


#if the given number is negative, convert it to a positive number and print it. Otherwise, print the given number.
if number < 0:
    number = number * (-1)
    
print(number)
