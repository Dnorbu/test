def add_student(name, age, grade, students_list, students_dict):
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}

def display_students(students_dict):
    print("Student Details:")
    for name, info in students_dict.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

def search_student(name, students_dict):
    if name in students_dict:
        info = students_dict[name]
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    else:
        print("Student not found.")

def remove_student(name, students_list, students_dict):
    if name in students_list:
        students_list.remove(name)
        del students_dict[name]
        print(f"{name} has been removed from the system.")
    else:
        print("Student not found.")

def main():
    students_list = []
    students_dict = {}

    while True:
        print("\nStudent Information Management System")
        print("1. Add a student")
        print("2. Display all students")
        print("3. Search for a student")
        print("4. Remove a student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = input("Enter student's grade: ")
            add_student(name, age, grade, students_list, students_dict)
            print("Student added successfully.")
        elif choice == '2':
            display_students(students_dict)
        elif choice == '3':
            name = input("Enter student's name to search: ")
            search_student(name, students_dict)
        elif choice == '4':
            name = input("Enter student's name to remove: ")
            remove_student(name, students_list, students_dict)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
