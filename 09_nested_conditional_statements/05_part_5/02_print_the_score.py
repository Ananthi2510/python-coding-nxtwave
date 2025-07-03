#Reads a distance and calculate the score

D = int(input())
bonus_score = 100

if D <= 50:
    score = D * 3 + bonus_score
    print(score)
elif D > 50 and D <= 100:
    score = 50 * 3 + (D - 50) * 5 + bonus_score
    print(score)
elif D > 100 and D <= 200:
    score = 50 * 3 + 50 * 5 + (D - 100) * 6 + bonus_score
    print(score)
elif D > 200:
    score = 50 * 3 + 50 * 5 + 100 * 6 + (D - 200) * 10 + bonus_score 
    print(score)
