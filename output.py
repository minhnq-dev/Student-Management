from domains.database import students, courses, marks

def list_students():
    if not students:
        print("\nNo students available.")
        return
    
    sorted_students = sorted(students, key=lambda s: s['gpa'], reverse=True)
    
    print("\nList of Students (Sorted by GPA)")
    for student in sorted_students:
        student_data = (student['id'], student['name'], student['dob'], student['gpa'])
        print("ID: %s | Name: %s | DoB: %s | GPA: %s" % student_data)

def list_courses():
    if not courses:
        print("\nNo courses available.")
        return
    
    print("\nList of Courses")
    for course in courses:
        course_data = (course['id'], course['name'], course['credits'])
        print("ID: %s | Name: %s | Credits: %s" % course_data)

def show_student_marks():
    if not marks:
        print("\nNo marks have been entered yet.")
        return

    selected_course_id = input("\nEnter the Course ID to view marks: ")
    
    if selected_course_id in marks and marks[selected_course_id]:
        print(f"\nMarks for Course ID: {selected_course_id}")
        for student in students:
            student_id = student['id']
            student_mark = marks[selected_course_id].get(student_id, "Not entered")
            print(f"Student: {student['name']} | Mark: {student_mark}")
    else:
        print("No marks found for this course, or invalid Course ID.")