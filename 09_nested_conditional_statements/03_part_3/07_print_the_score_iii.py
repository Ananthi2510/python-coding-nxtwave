#reads a distance D in km and calculates the total score.
#For the first 20 km (0 - 20 km), the score for each km is 2.
#For the next 40 km (21 - 60 km), the score for each km is 4.
#For the distance above 60 km, the score for each km is 6.
#Apart from the above scores, there is a bonus score of 30.

distance = int(input())

bonus_score = 30

first_20_score = 20 * 2
next_40_score = 40 * 4

if distance <= 20:
    score = distance * 2
elif distance <= 60:
    remaining_distance = distance - 20
    remaining_distance_score = remaining_distance * 4
    score = first_20_score + remaining_distance_score
else:
    remaining_distance = distance - 60
    remaining_distance_score = remaining_distance * 6
    score = first_20_score + next_40_score + remaining_distance_score

score = score + bonus_score
print(score)
