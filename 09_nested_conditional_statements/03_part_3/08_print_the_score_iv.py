#reads a distance D in km and calculates the total score.

For the first 40 km (0 - 40 km), the score for each km is 2.
For the next 20 km (41 - 60 km), the score for each km is 4.
For the next 60 km (61 - 120 km), the score for each km is 6.
For the distance above 120 km, the score for each km is 8.
Apart from the above scores, there is a bonus score of 50.

distance = int(input())

bonus_score = 50

first_40_score = 40 * 2
next_20_score = 20 * 4
next_60_score = 60 * 6

if distance <= 40:
    score = distance * 2
elif distance <= 60:
    remaining_distance = distance - 40
    remaining_distance_score = remaining_distance * 4
    score = first_40_score + remaining_distance_score
elif distance <= 120:
    remaining_distance = distance - 60
    remaining_distance_score = remaining_distance * 6
    score = first_40_score + next_20_score + remaining_distance_score
else:
    remaining_distance = distance - 120
    remaining_distance_score = remaining_distance * 8
    score = first_40_score + next_20_score + next_60_score + remaining_distance_score

score = score + bonus_score
print(score)
