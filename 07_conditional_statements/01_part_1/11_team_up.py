#Reads the scores
A = int(input())
B = int(input())

#checks if one of the scores is greater than 300 and the sum of the scores is less than 500. 
#If both conditions are met, we should print "Can team up". If not, we should print "Cannot team up".

if (A > 300 or B > 300) and (A + B < 500):
    print("Can team up")
else:
    print("Cannot team up")
