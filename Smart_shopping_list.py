items = {}

def add_item():
    name = input("Item: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per item: "))
    items[name] = (quantity, price)

def show_bill():
    total = 0

    print("\n--- Shopping List ---")
    for name, (quantity, price) in items.items():
        cost = quantity * price
        total += cost
        print(f"{name}: {quantity} x ₹{price} = ₹{cost}")

    print("Total: ₹", total)

while True:
    print("\n1. Add Item")
    print("2. View Bill")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        show_bill()
    elif choice == "3":
        break
