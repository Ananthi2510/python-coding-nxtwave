#reads the weight W of a box in kg and checks if the box is heavy or heavier

weight = int(input())

is_heavy = weight >= 30
is_heavier = weight >= 100

if is_heavier:
    print("Box is Heavier")
else:
    if is_heavy:
        print("Box is Heavy")
