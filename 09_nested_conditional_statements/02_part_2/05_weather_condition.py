#Display a customized message based on the given temperature

T = float(input())

if T < 0:
    print("Freezing weather")
elif 0 <= T < 10:
    print("Very Cold weather")
elif 10 <= T < 20:
    print("Cold weather")
elif 20 <= T < 30:
    print("Normal")
elif 30 <= T < 40:
    print("Hot")
elif T >= 40:
    print("Very Hot")
