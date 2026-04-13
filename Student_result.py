student = {
    "Aman": {"roll_no": "101", "marks": 75},
    "Riya": {"roll_no": "102", "marks": 32},
    "Rahul": {"roll_no": "103", "marks": 58}
}

while True:
    print("\n------ STUDENT MANAGER APP ------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")            

    choice = int(input("Enter your choice: "))

    # Add Student
    if choice == 1:
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        mark = int(input("Enter student marks: "))
        
        # ✅ FIX: store same structure
        student[name] = {
            "roll_no": roll_no,
            "marks": mark
        }

        print(f"{name} added successfully!")

    # View Student
    elif choice == 2:
        if not student:
            print("No students found.") 
        else:
            for name, details in student.items():
                print(f"Name: {name}, Roll No: {details['roll_no']}, Marks: {details['marks']}")

    # Check Result
    elif choice == 3:
        name = input("Enter student name to check result: ")
        if name in student:
            marks = student[name]["marks"]   # ✅ FIX
            if marks >= 40:
                print(f"{name} has passed with {marks} marks.")
            else:
                print(f"{name} has failed with {marks} marks.")
        else:
            print(f"No record found for {name}.")

    # Exit
    elif choice == 4:
        print("Exiting...........")
        break
    
    else:
        print("Invalid Input...!!! Please try again.")