#reads a distance D in km and calculates the total score.
#For the first 50 km (0 - 50 km), the score for each km is 3.
#For the distance above 50 km, the score for each km is 5.

distance = int(input())

first_50_score = 50 * 3

if distance <= 50:
    score = distance * 3
else:
    remaining_distance = distance - 50
    remaining_distance_score = remaining_distance * 5
    score = first_50_score + remaining_distance_score

print(score)
