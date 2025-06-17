#Reads maths and physics marks
m = int(input())
p = int(input())

#Checks if both are greater than 35 or sum of both marks is greater than or equal to 100
if (m > 35 and p > 35) or (m + p >= 100):
    print("Qualified")
else:
    print("Not Qualified")
