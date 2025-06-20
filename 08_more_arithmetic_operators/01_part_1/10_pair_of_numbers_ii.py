a = int(input())
b = int(input())
if (a % 3 == 0 and b % 3 == 0) and (a % 12 == 0 or b % 12 == 0):
    print("Pair")
else:
    print("Not a Pair")
