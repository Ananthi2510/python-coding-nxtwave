#Reads length and breadth
length = int(input())
breadth = int(input())

#Area of rectangle
area = length * breadth

#perimeter of rectangle
perimeter = 2 * (length + breadth)

#check if area of rectangle is less than or equal to perimeter of rectangle
result = area <= perimeter
print(result)
