#Reads two scores and compare the scores
A = int(input())
B = int(input())

if A > B:
    print("Win")
elif A == B:
    print("Draw")
elif A < B:
    print("Lose")
