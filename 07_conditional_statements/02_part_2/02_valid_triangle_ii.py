#Reads the three angles of a triangle

first_angle = int(input())
second_angle = int(input())
third_angle = int(input())

sum_of_three_angles = first_angle + second_angle + third_angle

if sum_of_three_angles == 180:
    print("*")
    print("*" * 2)
    print("*" * 3)
else:
    print("Not a Valid Triangle")
