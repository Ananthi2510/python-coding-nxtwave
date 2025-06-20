#to print if the given number is divisible by any of the lucky numbers 6, 3, 2 in decreasing order of priority 

n = int(input())
if n % 6 == 0:
    print("Number is divisible by 6")
elif n % 3 == 0:
    print("Number is divisible by 3")
elif n % 2 == 0:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")
    
