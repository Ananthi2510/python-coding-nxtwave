#eads a distance D in kilometers and calculates the score based on the following rules
#If D is less than or equal to 10, the score is D.
#If D is greater than 10, the score is the sum of 10 and (D - 10) * 3.

distance = int(input())

if distance <= 10:
    score = distance
else:
    remaining_distance = distance - 10
    score = 10 + (remaining_distance * 3)

print(score)
