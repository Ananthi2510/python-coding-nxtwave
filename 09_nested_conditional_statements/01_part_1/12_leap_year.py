#Reads a year and checks if the year is a leap year

y = int(input())

a = y % 400 == 0 
b = y % 4 == 0 and y % 100 != 0 

if a or b:
    print(a or b)
else:
    print(a and b)
