#reads an amount and prints the minimum number of 2000, 500, 200, 50, 20, 5, 2 and 1 rupees notes required for the given amount.

A = int(input())

twok_rem = A % 2000
twok = int((A - twok_rem) / 2000)

five_hun_rem = twok_rem % 500
five_hun = int((twok_rem - five_hun_rem) / 500)

two_hun_rem = five_hun_rem % 200 
two_hun = int((five_hun_rem - two_hun_rem) / 200)

fif_rem = two_hun_rem % 50 
fif = int((two_hun_rem - fif_rem) / 50)

twenty_rem = fif_rem % 20 
twenty = int((fif_rem - twenty_rem) / 20)

five_rem = twenty_rem % 5 
five = int((twenty_rem - five_rem) / 5)

two_rem = five_rem % 2 
two = int((five_rem - two_rem) / 2)

one = int(two_rem)


print("2000:" + str(twok) + " 500:" + str(five_hun) + " 200:" + str(two_hun) + " 50:" + str(fif) + " 20:" + str(twenty) + " 5:" + str(five) + " 2:" + str(two) + " 1:" + str(one))
