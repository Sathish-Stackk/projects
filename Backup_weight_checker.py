limit = float(input("Backpack weight limit (kg): "))
items = {}

while True:
    item = input("Item (done to finish): ")
    if item.lower() == "done":
        break
    weight = float(input("Weight (kg): "))
    items[item] = weight

total = sum(items.values())

print("Total weight:", total, "kg")

if total > limit:
    print("⚠️ Backpack is overweight!")
else:
    print("✅ Weight is within the limit.")
