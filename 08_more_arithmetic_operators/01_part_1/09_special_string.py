S = input()
s = S[0:3]
n = int(S[3:])

#Checks if all the given conditions are satisfied
#the first three characters of the string is NXT
#the remaining characters of the string contain a number, number is divisble by 2 or 7 

if s == "NXT" and (n % 2 == 0 or n % 7 == 0):
    print("Special String")
else:
    print("Not a Special String")
