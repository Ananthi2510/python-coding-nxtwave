#Reads three numbers
a = int(input())
b = int(input())
c = int(input())

#prints the greatest numnber
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print(a)
