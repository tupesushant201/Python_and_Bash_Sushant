students = {}

while True:
    print("\n1. Add student")
    print("2. Update grade")
    print("3. Print all grades")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print("Student already exists.")
        else:
            grade = input("Enter grade: ")
            students[name] = grade
            print("Student added.")
    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated.")
        else:
            print("Student not found.")
    elif choice == "3":
        if len(students) == 0:
            print("No students yet.")
        else:
            for name in students:
                print(name, ":", students[name])
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")