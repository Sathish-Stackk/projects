budget = float(input("Enter your budget: "))
total = 0

while True:
    item = input("Item name (done to finish): ")
    if item.lower() == "done":
        break

    price = float(input("Price: ₹"))
    total += price

    print(item, "added - ₹", price)
    print("Current total: ₹", total)

print("\nFinal total: ₹", total)
print("Remaining: ₹", budget - total)

if total > budget:
    print("⚠️ Budget exceeded!")
else:
    print("✅ Within budget!")
