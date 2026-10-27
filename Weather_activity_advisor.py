weather = input("Enter weather (sunny/rainy/cold): ").lower()
temp = float(input("Enter temperature: "))

if weather == "rainy":
    activity = "Stay indoors and read a book"
elif temp < 15:
    activity = "Have a warm drink and exercise indoors"
elif weather == "sunny":
    activity = "Go for a walk"
else:
    activity = "Outdoor activities are suitable"

print("Suggested activity:", activity)
