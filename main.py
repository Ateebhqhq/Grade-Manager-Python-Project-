import json
import numpy
import sys

class StudentManager:
    students_data = {}
    def __init__(students):
        students.students_data = {}

    def add_student(students, name): 
        if name in students.students_data:
            print(f"Student {name} already exists.")
            return
        
        else:
            students.students_data[name] = []
            print(f"Student {name} has been successfully added : )).\n")
    def add_grade(students, name, grade): 
        students.students_data[name] = [grade]
    def average (students, name): 
        grades = students.students_data[name]
        avg_grade = grades.avg()
        print("The average grade for {name} is {avg_grade}")
        
    def display_students(students):
        print(students.students_data)

    def save_to_file ( students , filename ): 
        with open(filename, "w") as file:
            json.dump(students.students_data, file)
    #def load_from_file ( filename ): 


if __name__ == "__main__":

    print("Welcome to the Student Grade Manager.")
    manager = StudentManager()
    while True:
        print("Please choose an option: \n")
        user_selection = input("1. Add student \n 2. Add grade \n 3. Show average for student \n 4. Show all students \n 5. Save to file \n 6. Load from file \n 7. Exit\n")
        match user_selection:
            case "1":
                name_input = input("Enter name: \n")
                manager.add_student(name_input)

            case "2":
                name_input = input("Enter name: \n")
                if name_input in manager.students_data:
                    grade_input = input("Enter grade: \n")
                    manager.add_grade(name_input, grade_input)

                else:
                    print("No such user exists with the name {name_input}.")

            case "3":
                name_input = input("Enter the student's name:")
                if name_input in students.students_data:
                    manager.average(name_input)

                else:
                    print("The student {name} does not exist.")

            case "7":
                print("The program is shutting off. Ciao :( ")
                sys.exit(1)