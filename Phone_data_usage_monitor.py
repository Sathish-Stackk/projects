def check_data(used, limit):
    remaining = limit - used

    if remaining <= 0:
        return "Data limit exceeded"
    elif remaining <= limit * 0.2:
        return f"Low data: {remaining:.1f} GB remaining"
    return f"Data remaining: {remaining:.1f} GB"

limit = float(input("Monthly data limit (GB): "))
used = float(input("Data used (GB): "))

print("\nData Status:", check_data(used, limit))
