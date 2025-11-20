# # -----------------------------------------
# # Student Information & Grade Management System
# # -----------------------------------------

# # Using Unicode string
# welcome_msg = "🧑‍🎓 Welcome to Student Grade Management System 🧑‍🏫"
# print(welcome_msg)

# students = []   # List to store student dictionaries

# def calculate_grade(marks):
#     """Function to calculate grade based on marks."""
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     elif marks >= 40:
#         return "D"
#     else:
#         return "F"

# while True:
#     print("\n--- Enter Student Details ---")
    
#     # Reading from keyboard
#     name = input("Enter student name: ")
#     roll = input("Enter roll number: ")

#     # Math operators
#     marks = float(input("Enter marks out of 100: "))

#     # Using a dictionary to store student info
#     student = {
#         "name": name,
#         "roll": roll,
#         "marks": marks,
#         "grade": calculate_grade(marks)
#     }

#     students.append(student)

#     ch = input("Do you want to add another student? (yes/no): ")
#     if ch.lower() != "yes":
#         break

# # Writing data to a text file
# with open("student_records.txt", "w") as file:
#     file.write("Student Records\n")
#     file.write("-----------------------\n")
    
#     for stu in students:  # Using for loop
#         file.write(f"Name: {stu['name']}, Roll: {stu['roll']},










# -----------------------------------------
# Student Information & Grade Management System
# -----------------------------------------

# Using Unicode string
welcome_msg = "🧑‍🎓 Welcome to Student Grade Management System 🧑‍🏫"
print(welcome_msg)

students = []   # List to store student dictionaries

def calculate_grade(marks):
    """Function to calculate grade based on marks."""
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

while True:
    print("\n--- Enter Student Details ---")
    
    # Reading from keyboard
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    # Math operators
    marks = float(input("Enter marks out of 100: "))

    # Using a dictionary to store student info
    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "grade": calculate_grade(marks)
    }

    students.append(student)

    ch = input("Do you want to add another student? (yes/no): ")
    if ch.lower() != "yes":
        break

# Writing data to a text file
with open("student_records.txt", "w") as file:
    file.write("Student Records\n")
    file.write("-----------------------\n")
    
    for stu in students:  # Using for loop
        file.write(f"Name: {stu['name']}, Roll: {stu['roll']}, Marks: {stu['marks']}, Grade: {stu['grade']}\n")

print("\n✅ Student records have been saved to 'student_records.txt'.")