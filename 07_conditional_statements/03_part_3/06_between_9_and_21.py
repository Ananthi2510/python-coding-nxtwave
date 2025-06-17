#reads three numbers
a = int(input())
b = int(input())
c = int(input())

#Checks if any of the numbers is between 9 and 21
is_between = (9 < a < 21) or (9 < b < 21) or (9 < c < 21)

if is_between:
    print(is_between)
else:
    print(1 != 1)
