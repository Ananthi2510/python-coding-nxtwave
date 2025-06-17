#Reads a three digit number
n = input()

#Checks if both the conditions are satisfied
#any of the digits of the number is not equal to 5 
#the number is between 300 and 700

if (n[0] != "5" or n[1] != "5" or n[2] != "5") and (300 < N < 700):
    print("Valid Number")
else:
    print("Not a Valid Number")
