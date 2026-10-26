distance = float(input("Enter distance (km): "))
age = int(input("Enter your age: "))

if distance <= 5:
    fare = 10
elif distance <= 15:
    fare = 20
else:
    fare = 30

if age < 12:
    fare *= 0.5
elif age >= 60:
    fare *= 0.7

print("Distance:", distance, "km")
print("Final Bus Fare: ₹", fare)
