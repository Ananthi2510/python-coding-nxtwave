#reads cost price CP and sellings price SP of a product and compares both

cost_price = int(input())
selling_price = int(input())

if selling_price > cost_price :
    print("Profit")
elif cost_price > selling_price :
    print("Loss")
else:
    print("No Profit - No Loss")
