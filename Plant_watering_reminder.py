from datetime import date

plant = input("Plant name: ")
days = int(input("Watering interval (days): "))
last = input("Last watered (YYYY-MM-DD): ")

last_date = date.fromisoformat(last)
today = date.today()
passed = (today - last_date).days

print("\nPlant:", plant)
print("Days since watering:", passed)

if passed >= days:
    print("💧 Water the plant today!")
else:
    print("🌿 Plant is fine for now.")
