def average():
    grades = []
    
    while True:
        user_input = input("Enter a grade (press Enter to finish): ")
        
        if user_input == "":
            break
        
        try:
            grade = float(user_input)
            grades.append(grade)
        except ValueError:
            print("Please enter a valid number.")
    
    if len(grades) == 0:
        return "No grades entered."
    else:
        total_grades = sum(grades)
        average = total_grades / len(grades)
        print(average)

average()
