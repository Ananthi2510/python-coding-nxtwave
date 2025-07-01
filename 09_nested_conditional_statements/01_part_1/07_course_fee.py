#Reads a mark of a student

M = int(input())
 
if M >= 90:
    print("Discount is 200")
elif M >= 50 and M <= 90:
    print("Discount is 100")
elif M <= 50:
    print("No Discount")
