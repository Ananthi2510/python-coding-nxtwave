#Reads a number N and prints a Right angled triangle of N rows using stars(*) and pluses(+)

N = int(input())
counter = 1
while counter <= N-1:
    print("* " * counter)
    counter = counter + 1
if counter == N:
    print("+ " * counter)
