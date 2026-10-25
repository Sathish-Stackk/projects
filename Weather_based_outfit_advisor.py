def outfit_advisor(temp, rain):
    if rain == "yes":
        return "Carry an umbrella and wear waterproof footwear."
    elif temp < 15:
        return "Wear a jacket and warm clothes."
    elif temp < 25:
        return "Wear comfortable full-sleeve clothes."
    elif temp < 35:
        return "Wear light cotton clothes."
    return "Wear loose, breathable clothes and stay hydrated."

temperature = float(input("Temperature (°C): "))
rain = input("Is it raining? (yes/no): ").lower()

print("\nAdvice:", outfit_advisor(temperature, rain))
