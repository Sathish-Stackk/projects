def crop_advisor(moisture, temperature, ph):
    if moisture < 30:
        return "Irrigation required"
    elif temperature > 35:
        return "High temperature - provide shade"
    elif ph < 5.5 or ph > 7.5:
        return "Check soil pH"
    return "Crop conditions look healthy"

print("🌱 Crop Health Advisor")

moisture = float(input("Soil moisture (%): "))
temperature = float(input("Temperature (°C): "))
ph = float(input("Soil pH: "))

print("\nRecommendation:", crop_advisor(moisture, temperature, ph))
