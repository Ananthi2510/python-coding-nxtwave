#Reads two coupon codes
a = input()
b = input()

#Chceks if the first three characters of one of the coupon codes is equal to "DIS"
if a[0:3] == "DIS" or b[0:3] == "DIS":
    print("Discount")
else:
    print("No Discount")
