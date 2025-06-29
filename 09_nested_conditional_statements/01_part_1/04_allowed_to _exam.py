hall_ticket = input()
identification = input()

has_hall_ticket = (hall_ticket == "Y")
has_identification = (identification == "Y")

# to check if the student has a hall ticket or identification card
if has_hall_ticket:
    print("Allowed to Exam - Has Hall ticket")
else:
    if has_identification:
        print("Allowed to Exam - Has Identification Card")
