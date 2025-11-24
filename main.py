import json
import numpy
import sys
import time
import os

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
    
    def del_student(students, name):
        if name in students.students_data:
            del students.students_data[name]
            print(f"The student, '{name}', has been successfully deleted.\n")

        else:
            print(f"The student with the name, {name}, not found. :( ")
            return
    
    def add_grade(students, name, grade): 
        students.students_data[name].append(float(grade))
    
    def del_grade(students, name, grade):
        students.students_data[name].remove(grade)
    
    def average (students, name): 
        grades = students.students_data[name]
        avg_grade = numpy.mean(grades)
        print(f"The average grade for {name} is {avg_grade} \n ")
        time.sleep(1)
        


    def save_to_file(students, filename): 
        with open(filename, "w") as file:
            json.dump(students.students_data, file)
            print(f"{filename} has been successfully saved. \n ")

    def load_from_file(students, filename):

        with open(filename, "r") as file:
            students.students_data = json.load(file)
            print(f"{filename} has been successfully loaded. \n ")
           


if __name__ == "__main__":
    print("\n======================================================")
    print("Welcome to the Student Grade Manager.")
    print("======================================================")
    manager = StudentManager()
    while True:
        try:
            print("\n \n Please choose an option: \n")
            user_selection = input("\n 1. Add/delete student \n 2. Add/delete grade \n 3. Show average for student \n 4. Show all students \n 5. Save to file \n 6. Load from file \n 7. Exit\n")
            match user_selection:
                case "1":
                    user_input = input("\n Choose an option: \n 1. Add a student \n 2. Delete a student \n ")
                    match user_input:
                        case "1":
                            name_input = input("Enter name: \n")
                            manager.add_student(name_input)

                        case "2":
                            name_input = input("Enter name: \n")
                            manager.del_student(name_input)


                case "2":
                    user_input = input("\n Choose an option: \n 1. Add a grade \n 2. Delete a grade \n ")
                    match user_input:
                        case "1":
                            name_input = input("Enter name: \n")
                            if name_input in manager.students_data:
                                print(f"The data for the chosen student. \n")
                                personal_student_data = manager.students_data[name_input]
                                print(personal_student_data)
                                grade_input = float(input("Enter grade: \n"))
                                if 0 <= grade_input <= 100:
                                    manager.add_grade(name_input, grade_input)
                                else:
                                    print(f"Enter a valid grade between 0-100 :)")

                            else:
                                print("No such user exists with the name {name_input}.")
                                time.sleep(1)

                        case "2":
                            name_input = input("Enter name: \n")
                            if name_input in manager.students_data:
                                print(f"The data for the chosen student. \n")
                                personal_student_data = manager.students_data[name_input]
                                print(personal_student_data)
                                grade_input = float(input("Enter grade: \n"))
                                if 0 <= grade_input <= 100:
                                    manager.del_grade(name_input, grade_input)
                                elif grade_input not in students.students_data[name_input]:
                                    print(f"The grade {grade_input} does not exist.")
                                else:
                                    print(f"Enter a valid grade between 0-100 :)")
                                    time.sleep(1)



                    

                case "3":
                    name_input = input("Enter the student's name:")
                    if name_input in manager.students_data:
                        manager.average(name_input)
                        time.sleep(1)

                    else:
                        print(f"The student {name} does not exist.")

                case "4":
                    whole_students_data = manager.students_data
                    print("Name:       Grades:")
                    print(whole_students_data)
                    time.sleep(1)

                case "5":
                    input_filename = input("\nWhat name do you want to give to your file? \n")
                    manager.save_to_file(input_filename)

                case "6":
                    listed_directories = os.listdir()
                    print(listed_directories)
                    input_filename = input("\n Which file do you want to load?\n")
                    manager.load_from_file(input_filename)

                case "7":
                    print("The program is shutting off. Ciao :( ")
                    sys.exit(1)

        except KeyboardInterrupt as e:
            print("\n The program is shutting off bruh :( ")
            sys.exit(1)