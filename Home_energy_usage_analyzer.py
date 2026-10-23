def energy_report(units):
    if units <= 100:
        return "Low usage"
    elif units <= 250:
        return "Moderate usage"
    elif units <= 400:
        return "High usage"
    return "Very high usage"

appliances = {}

for i in range(3):
    name = input(f"Appliance {i + 1}: ")
    units = float(input("Units consumed: "))
    appliances[name] = units

total = sum(appliances.values())

print("\n--- Energy Report ---")
for name, units in appliances.items():
    print(name, ":", units, "units")

print("Total:", total, "units")
print("Status:", energy_report(total))
