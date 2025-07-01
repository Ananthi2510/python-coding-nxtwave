#reads two numbers A, and B, and 

#prints the relation between A and B by checking if any of the given conditions is satisfied:
#A is equal to B (A == B)
#A is greater than B (A > B)
#A is less than B (A < B)

A = int(input())
B = int(input())

if A == B:
    print("A == B")
elif A > B:
    print("A > B")
elif A < B:
    print("A < B")
