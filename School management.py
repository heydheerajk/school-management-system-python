
# SCHOOL MANAGEMENT SYSTEM

# Admin login details
admin = {
    "admin": "123",
    "owner": "456"
}

# Store student records
students = []

# Admin login
print("=== WELCOME TO SK SCHOOL ===")

attempts = 3
logged_in = False

while attempts > 0:
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username in admin and admin[username] == password:
        print("\nLogin successful!")
        logged_in = True
        break
    else:
        attempts -= 1
        print("Incorrect username or password.")
        print("Attempts remaining:", attempts)

if logged_in:

    while True:
        print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
        print("1. New Student Admission")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Record Attendance")
        print("5. View Attendance")
        print("6. Add Student Marks")
        print("7. View Marks")
        print("8. Record Fee Payment")
        print("9. View Fee Report")
        print("10. Exit")

        choice = input("Enter your choice: ")

        # NEW ADMISSION
        if choice == "1":
            roll = input("Enter student roll number: ")

            if any(s["roll"] == roll for s in students):
                print("Roll number already exists!")
                continue

            name = input("Enter student name: ")
            class_name = input("Enter student class: ")
            total_fee = float(input("Enter total school fee: "))

            student = {
                "roll": roll,
                "name": name,
                "class": class_name,
                "attendance": {},
                "marks": {},
                "total_fee": total_fee,
                "payments": []
            }

            students.append(student)
            print("Student admitted successfully!")

        # VIEW ALL STUDENTS
        elif choice == "2":
            if not students:
                print("No students registered.")
            else:
                for s in students:
                    print(
                        "Roll:", s["roll"],
                        "| Name:", s["name"],
                        "| Class:", s["class"]
                    )

        # SEARCH STUDENT
        elif choice == "3":
            roll = input("Enter roll number: ")
            found = False

            for s in students:
                if s["roll"] == roll:
                    print("Name:", s["name"])
                    print("Roll:", s["roll"])
                    print("Class:", s["class"])
                    found = True
                    break

            if not found:
                print("Student not found.")

        # RECORD ATTENDANCE
        elif choice == "4":
            roll = input("Enter roll number: ")

            for s in students:
                if s["roll"] == roll:
                    day = input("Enter date (YYYY-MM-DD): ")
                    status = input("Present or Absent (P/A): ").upper()

                    if status in ("P", "A"):
                        s["attendance"][day] = (
                            "Present" if status == "P" else "Absent"
                        )
                        print("Attendance saved.")
                    else:
                        print("Invalid attendance status.")
                    break
            else:
                print("Student not found.")

        # VIEW ATTENDANCE
        elif choice == "5":
            roll = input("Enter roll number: ")

            for s in students:
                if s["roll"] == roll:
                    records = s["attendance"]

                    if not records:
                        print("No attendance records.")
                    else:
                        present = 0

                        for day, status in records.items():
                            print(day, ":", status)
                            if status == "Present":
                                present += 1

                        total = len(records)
                        percentage = present / total * 100

                        print("Attendance:", round(percentage, 2), "%")
                    break
            else:
                print("Student not found.")

        # ADD OR UPDATE MARKS
        elif choice == "6":
            roll = input("Enter roll number: ")

            for s in students:
                if s["roll"] == roll:
                    subject = input("Enter subject name: ")
                    maximum = float(input("Enter maximum marks: "))
                    score = float(input("Enter marks obtained: "))

                    if maximum <= 0 or score < 0 or score > maximum:
                        print("Invalid marks.")
                    else:
                        s["marks"][subject] = {
                            "score": score,
                            "maximum": maximum
                        }
                        print("Marks saved.")
                    break
            else:
                print("Student not found.")

        # VIEW MARKS
        elif choice == "7":
            roll = input("Enter roll number: ")

            for s in students:
                if s["roll"] == roll:
                    if not s["marks"]:
                        print("No marks recorded.")
                    else:
                        scored = 0
                        maximum = 0

                        for subject, result in s["marks"].items():
                            print(
                                subject, ":",
                                result["score"], "/",
                                result["maximum"]
                            )
                            scored += result["score"]
                            maximum += result["maximum"]

                        print("Total:", scored, "/", maximum)
                        print("Percentage:", round(scored / maximum * 100, 2), "%")
                    break
            else:
                print("Student not found.")

        # RECORD FEE PAYMENT
        elif choice == "8":
            roll = input("Enter roll number: ")

            for s in students:
                if s["roll"] == roll:
                    paid = sum(s["payments"])
                    balance = s["total_fee"] - paid

                    print("Total fee:", s["total_fee"])
                    print("Already paid:", paid)
                    print("Remaining fee:", balance)

                    amount = float(input("Enter payment amount: "))

                    if amount <= 0:
                        print("Payment must be greater than zero.")
                    elif amount > balance:
                        print("Payment exceeds remaining fee.")
                    else:
                        s["payments"].append(amount)
                        print("Payment recorded successfully.")
                    break
            else:
                print("Student not found.")

        # VIEW FEE REPORT
        elif choice == "9":
            roll = input("Enter roll number: ")

            for s in students:
                if s["roll"] == roll:
                    paid = sum(s["payments"])
                    balance = s["total_fee"] - paid

                    print("Student:", s["name"])
                    print("Total fee:", s["total_fee"])
                    print("Paid:", paid)
                    print("Balance:", balance)
                    print("Status:", "PAID" if balance == 0 else "PENDING")
                    break
            else:
                print("Student not found.")

        # EXIT
        elif choice == "10":
            print("Thank you for using SK School!")
            break

        else:
            print("Invalid choice. Enter 1 to 10.")

else:
    print("Access denied.")
    