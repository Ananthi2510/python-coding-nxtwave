#read the input marks and then check the conditions for each grade
#f the marks fall in the range of a particular grade, we will print that grade.

marks = float(input())

if marks > 85:
    print("A")
elif marks > 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("F")
