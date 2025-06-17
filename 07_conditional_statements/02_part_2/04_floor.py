#Reads a rom number which is in the format of R1, R35, etc
room_number = input()

number = room_number[1:]
number = int(number)

#hecks if the Number in the given Room Number is less than 30.
if (number < 30):
    print("Ground Floor")
else:
    print("Not Ground Floor")
