#given number of days as input
#convert number of days into years , weeks and days 

n = int(input())

a = n % 365 
y = int((n-a) / 365)
print(y)

b = a % 7
w = int((a - b) / 7)
print(w)

d = n - (y * 365) - (w * 7)
print(d)
