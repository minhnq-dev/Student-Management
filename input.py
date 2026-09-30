from domains.database import students, courses, marks, round_down_mark, calculate_all_gpa
from output import list_courses

def input_students():
    num_student = int(input("Insert number of students in the class: "))
    for i in range(num_student):
        print(f"\n[Student {i+1}]")
        name = input("Name: ")
        student_id = input("Student ID: ")
        dob = input("Date of Birth (DD/MM/YYYY): ")

        students.append({"name": name, "id": student_id, "dob": dob, "gpa": 0.0})

    print("Student's information saved successfully.")

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for j in range(num_courses):
        print(f"\n[Course {j+1}]")
        course_name = input("Name of the course: ")
        course_id = input("Course ID: ")
        credits = int(input("Number of credits: "))

        courses.append({"name": course_name, "id": course_id, "credits": credits})
        marks[course_id] = {}
    print("Course information saved.")

def input_marks():
    if not courses or not students:
        print("Please input both students and courses first.")
        return
    
    list_courses()
    selected_course_id = input("Enter the course ID you want to put marks for: ")
    
    if any(course['id'] == selected_course_id for course in courses):
        for student in students:
            while True:
                try:
                    mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
                    mark = round_down_mark(mark)
                    marks[selected_course_id][student['id']] = mark
                    break
                except ValueError:
                    print("Invalid input. Please enter a numerical mark.")
        
        calculate_all_gpa()
        print("Marks saved and GPA updated successfully!")
    else:
        print("Invalid Course ID.")