#Reads the three angles of a triangle 

a = int(input())
b = int(input())
c = int(input())

#the triangle is valid if the sum of the angles is 180
if a + b + c == 180:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
