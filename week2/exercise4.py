score = int(input("Please enter your score (between 0 and 100): "))

if score > 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Needs Improvement")
else:
    print("Failed!")
