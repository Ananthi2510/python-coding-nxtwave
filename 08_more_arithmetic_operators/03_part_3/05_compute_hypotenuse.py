#reads two sides of a right_angled triangle
#prints the hypotenuse of that triangle

A = int(input())
B = int(input())

hypotenuse = ((A ** 2) + (B ** 2)) ** 0.5
print(int(hypotenuse))
