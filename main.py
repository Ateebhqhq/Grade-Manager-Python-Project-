import json
import numpy

class StudentManager:
    students_data = {}
    def __init__(students):
        students.students_data = {}

    def add_student(students ,name): 
        if name in students.students_data:
            print(f"Student {name} already exists.")
            return
        
        else:
            students_data[name] = []
    def add_grade ( students , name , grade ): 
        students_data[name] = [grade]
    #def average ( students , name ): 
        
    #def save_to_file ( students , filename ): 
    #def load_from_file ( filename ): 


if __name__ == "__main__":

    print("Welcome to the Student Grade Manager.")
    manager = StudentManager()
    while True:
        print("Please choose an option: ")
        user_selection = input("1. Add student \n 2. Add grade \n 3. Show average for student \n 4. Show all students \n 5. Save to file \n 6. Load from file \n 7. Exit")
        match user_selection:
            case "1":
                name_input = input("Enter name: \n")
                manager.add_student(name_input)

            case "2":
                name_input = input("Enter name: \n")
                if name_input in students_data:
                    grade_input = input("Enter grade: \n")
                    add_grade(s1, name_input, grade_input)

                else:
                    print("No such user exists with the name {name_input}.")