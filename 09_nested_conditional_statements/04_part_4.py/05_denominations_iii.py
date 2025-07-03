#Reads an amount and prints the minimum number of 500, 50, 10 and 1 rupees notes required for the given amount

A = int(input())

five_hun_rem = A % 500
five_hun = int((A - five_hun_rem) / 500)

fif_rem = five_hun_rem % 50 
fif = int((five_hun_rem - fif_rem) / 50)

ten_rem = fif_rem % 10
ten = int((fif_rem - ten_rem) / 10)

one = int(ten_rem)

print("500: " + str(five_hun) + " 50: " + str(fif) + " 10: " + str(ten) + " 1: " + str(one))
