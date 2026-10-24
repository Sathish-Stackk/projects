from datetime import datetime

def days_until_birthday(day, month):
    today = datetime.now()
    birthday = datetime(today.year, month, day)

    if birthday.date() < today.date():
        birthday = datetime(today.year + 1, month, day)

    return (birthday.date() - today.date()).days

day = int(input("Birthday day: "))
month = int(input("Birthday month: "))

print("Days remaining:", days_until_birthday(day, month))
