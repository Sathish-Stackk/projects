def attendance_status(total, present):
    percentage = (present / total) * 100

    if percentage >= 75:
        return percentage, "Eligible"
    return percentage, "Shortage"

total = int(input("Total classes: "))
present = int(input("Classes attended: "))

percentage, status = attendance_status(total, present)

print("Attendance:", round(percentage, 2), "%")
print("Status:", status)
