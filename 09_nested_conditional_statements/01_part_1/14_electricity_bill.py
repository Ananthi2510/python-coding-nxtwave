#to calculate the electricity bill for a household, based on the units of electricity the household consumed. 

#The price for unit varies based on the slab. The charges per unit for different slabs are as mentioned below:

#For the first 50 units (0-50), the charge is 2/unit
#For the next 100 units (51-150), the charge is 3/unit
#For the next 100 units (151-250), the charge is 5/unit
#For above 250 units (251 and above), the charge is 8/unit

#there is also an additional surcharge of 20% on the total amount is added to the bill.

units = int(input())
price = 0

if units > 0 and units <= 50:
    price = 2 * units
    
elif units >= 51 and units <= 150:
    price = 2 * 50 + 3 * (units - 50)
    
elif units >= 151 and units <= 250:
    price = 2 * 50 + 3 * 100 + 5 * (units- 150)
    
elif units > 250:
    price = 2 * 50 + 3 * 100 + 5 * 100 + 8 * (units - 250)

bill_amount = price + (0.2 * price)
print(bill_amount)
    
