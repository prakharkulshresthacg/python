age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

age_ok = age >= 18 and age <= 25
marks_ok = marks >= 85
attendance_ok = attendance >= 75
income_ok = income <= 300000

if age_ok and marks_ok and attendance_ok and income_ok:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")
    if not age_ok:
        print("Reason: Age not in range 18-25")
    if not marks_ok:
        print("Reason: Marks below 85")
    if not attendance_ok:
        print("Reason: Attendance below 75%")
    if not income_ok:
        print("Reason: Family income above 300000")
