#Reads an amount and prints the minimum number of 100, 50, 10 and 1 rupee notes required for the given amount 

A = int(input())

hun_rem = A % 100
hun = int((A - hun_rem) / 100)

fif_rem = (hun_rem) % 50
fif = int((hun_rem - fif_rem) / 50)

ten_rem = (fif_rem) % 10 
ten = int((fif_rem - ten_rem) / 10)

one = int(ten_rem)

print("100:" + str(hun))
print("50:" + str(fif))
print("10:" + str(ten))
print("1:" + str(one))
