Sub1 = float(input("Enter Marks for Sub1: "))
Sub2 = float(input("Enter Marks for Sub2: "))
Sub3 = float(input("Enter Marks for Sub3: "))
Sub4 = float(input("Enter Marks for Sub4: "))
Sub5 = float(input("Enter Marks for Sub5: "))

TotalMarks = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
Percentage = TotalMarks / 5

print("Total Marks =", TotalMarks)
print("Percentage =", Percentage)

# Grades
if Percentage > 90:
    print("O Grade")
elif Percentage >= 80:
    print("A+ Grade")
elif Percentage >= 70:
    print("A Grade")
elif Percentage >= 60:
    print("B+ Grade")
elif Percentage >= 50:
    print("B Grade")
elif Percentage >= 40:
    print("C Grade")
else:
    print("Fail")