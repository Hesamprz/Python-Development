grades = []

while True:
    grade = input("Enter the number or 'quit': ")
    if grade.lower() == "quit":
        break
    try:
        num = float(grade)
        grades.append(num)
    except ValueError:
        print("ValueError!")

average = sum(grades) / len(grades)
print(f"The average is: {average}")
