def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return duplicates

nums = list(map(int, input("Enter numbers: ").split()))
duplicates = find_duplicates(nums)

if duplicates:
    print("Duplicate numbers:", sorted(duplicates))
else:
    print("No duplicates found")
