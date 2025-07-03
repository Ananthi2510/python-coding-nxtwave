#Reads attendance percentage and medical status from the user.
#To check if the student is allowed to write the exam based on their attendance percentage and medical report status. 

attendance = input()
medical_reason = input()

length = len(attendance)

attendance = attendance[: (length - 1)]
attendance = int(attendance)

if attendance >= 75:
    print("Allowed to write exam")
elif attendance < 75 and medical_reason == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")
