student_marks = {
    "Aarav": 85,
    "Divya": 92,
    "Ishaan": 78,
    "Meera": 90,
    "Rohan": 88
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found .")

