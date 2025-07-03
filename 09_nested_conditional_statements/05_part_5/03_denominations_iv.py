#Reads an amount and prints the minimum number of 100, 50, 20 and 10 rupee notes required for the given amount.

A = int(input())

hun_rem = A % 100
hun = int((A - hun_rem) / 100)

fif_rem = hun_rem % 50
fif = int((hun_rem - fif_rem) / 50)

twenty_rem = fif_rem % 20
twenty = int((fif_rem - twenty_rem) / 20)

ten_rem = twenty_rem % 10 
ten = int((twenty_rem - ten_rem) / 10)

print("100 Notes: " + str(hun))
print("50 Notes: " + str(fif))
print("20 Notes: " + str(twenty))
print("10 Notes: " + str(ten))
