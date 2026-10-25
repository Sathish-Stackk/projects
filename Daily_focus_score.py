def focus_score(study, sleep, distractions):
    score = study * 2 + sleep - distractions * 2

    if score >= 15:
        return score, "Excellent focus"
    elif score >= 8:
        return score, "Good focus"
    return score, "Needs improvement"

study = int(input("Study hours: "))
sleep = int(input("Sleep hours: "))
distractions = int(input("Number of major distractions: "))

score, result = focus_score(study, sleep, distractions)

print("\nFocus Score:", score)
print("Result:", result)
