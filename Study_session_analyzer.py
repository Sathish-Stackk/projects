sessions = {}

while True:
    subject = input("Subject (done to finish): ")
    if subject.lower() == "done":
        break

    minutes = int(input("Study minutes: "))
    sessions[subject] = sessions.get(subject, 0) + minutes

print("\n--- Study Report ---")

total = 0
for subject, minutes in sessions.items():
    print(subject, ":", minutes, "minutes")
    total += minutes

print("Total study time:", total, "minutes")
print("Hours:", round(total / 60, 2))
