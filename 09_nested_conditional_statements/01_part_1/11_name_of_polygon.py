#reads the number N and prints the name of the polygon based on the N number of sides

n = int(input())

if n < 3:
    print("Not Polygon")
elif n == 3:
    print("Triangle")
elif n == 4:
    print("Quadrilateral")
elif n == 5:
    print("Pentagon")
else:
    print("Big Polygon")
