students = {
    "hesam": {"name": "Hesam", "family": "Pourreza", "class": 201},
    "reza": {"name": "Reza", "family": "Heydari", "class": 202},
    "parsa": {"name": "Parsa", "family": "Saadat", "class": 203}
}

def find_student_info():
    first_name = input("Enter the student's first name: ")
    try:
        print(f"Name: {students[first_name]["name"]}")
        print(f"Family: {students[first_name]["family"]}")
        print(f"Class: {students[first_name]["class"]}")
    except KeyError:
        print(f"Student {first_name} not found!")

find_student_info()