#Find the smallest numbers among the three numbers A, B and C

A = int(input())
B = int(input())
C = int(input())

if A < B and A < C:
    print(A)
elif B < C and B < A:
    print(B)
elif C < A and C < B:
    print(C)
else:
    print(A)
