#Reads an amount and prints the minimum number of 5 and 1 rupees notes required for the given amount

amount = int(input())

no_of_5s = amount // 5
no_of_1s = amount % 5

print("5:" + str(no_of_5s))
print("1:" + str(no_of_1s))
