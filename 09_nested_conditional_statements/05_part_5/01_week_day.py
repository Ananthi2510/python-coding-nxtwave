#Reads a number and checks if the day is week start, weekend, or midweek

day_number = int(input())

if day_number == 1 or day_number == 2:
    print("Week Start")
elif day_number == 3 or day_number == 4 or day_number == 5:
    print("Midweek")
else:
    print("Weekend")
