#Reads three sides of a triangle
a = int(input())
b = int(input())
c = int(input())

#Checks if the sum of any two sides of a triangle is always greater than the third side
if a + b > c and b + c > a and a + c > b:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
