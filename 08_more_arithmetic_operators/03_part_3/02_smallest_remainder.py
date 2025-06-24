#Find the remainder when A is divided by B (A % B).
#Find the remainder when B is divided by A (B % A).
#The smallest of these two remainders is then printed as the output.

A = int(input())
B = int(input())

if (A % B) < (B % A):
  print(A % B)
else:
    print(B % A)
