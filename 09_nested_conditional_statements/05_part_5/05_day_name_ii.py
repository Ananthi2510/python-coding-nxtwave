#Give the weekday of the first day of the month , determine the day of the week of the given date in that month

d = input()
n = int(input())

if d == "Monday":
    if (n % 7) == 1:
        print("Monday")
    elif (n % 7) == 2:
        print("Tuesday")
    elif (n % 7) == 3:
        print("Wednesday")
    elif (n % 7) == 4:
        print("Thursday")
    elif (n % 7) == 5:
        print("Friday")
    elif (n % 7) == 6:
        print("Saturday")
    elif (n % 7) == 0:
        print("Sunday")
        
if d == "Tuesday":
    if (n % 7) == 0:
        print("Monday")
    elif (n % 7) == 1:
        print("Tuesday")
    elif (n % 7) == 2:
        print("Wednesday")
    elif (n % 7) == 3:
        print("Thursday")
    elif (n % 7) == 4:
        print("Friday")
    elif (n % 7) == 5:
        print("Saturday")
    elif (n % 7) == 6:
        print("Sunday")
        
if d == "Wednesday":
    if (n % 7) == 0:
        print("Tuesday")
    elif (n % 7) == 1:
        print("Wednesday")
    elif (n % 7) == 2:
        print("Thursday")
    elif (n % 7) == 3:
        print("Friday")
    elif (n % 7) == 4:
        print("Saturday")
    elif (n % 7) == 5:
        print("Sunday")
    elif (n % 7) == 6:
        print("Monday")
        
if d == "Thursday":
    if (n % 7) == 5:
        print("Monday")
    elif (n % 7) == 6:
        print("Tuesday")
    elif (n % 7) == 0:
        print("Wednesday")
    elif (n % 7) == 1:
        print("Thursday")
    elif (n % 7) == 2:
        print("Friday")
    elif (n % 7) == 3:
        print("Saturday")
    elif (n % 7) == 4:
        print("Sunday")
        
if d == "Friday":
    if (n % 7) == 4:
        print("Monday")
    elif (n % 7) == 5:
        print("Tuesday")
    elif (n % 7) == 6:
        print("Wednesday")
    elif (n % 7) == 0:
        print("Thursday")
    elif (n % 7) == 1 :
        print("Friday")
    elif (n % 7) == 2:
        print("Saturday")
    elif (n % 7) == 3:
        print("Sunday")
        
if d == "Saturday":
    if (n % 7) == 3:
        print("Monday")
    elif (n % 7) == 4:
        print("Tuesday")
    elif (n % 7) == 5:
        print("Wednesday")
    elif (n % 7) == 6:
        print("Thursday")
    elif (n % 7) == 0:
        print("Friday")
    elif (n % 7) == 1 :
        print("Saturday")
    elif (n % 7) == 2:
        print("Sunday")
    
if d == "Sunday":
    if (n % 7) == 2:
        print("Monday")
    elif (n % 7) == 3:
        print("Tuesday")
    elif (n % 7) == 4:
        print("Wednesday")
    elif (n % 7) == 5:
        print("Thursday")
    elif (n % 7) == 6:
        print("Friday")
    elif (n % 7) == 0:
        print("Saturday")
    elif (n % 7) == 1:
        print("Sunday")
        
