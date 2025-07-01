#to print a greeting message based on the given time

t = int(input())

if t >= 4 and t < 12:
    print("Good Morning")
elif t >= 12 and t < 16:
    print("Good Afternoon")
elif t >= 16 and t < 20:
    print("Good Evening")
elif t >= 20 or t < 4:
    print("Good Night")
