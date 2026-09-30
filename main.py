from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_student_marks

def main():
    while True:
        print("STUDENT MARK MANAGEMENT")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students (by GPA)")
        print("5. List courses")
        print("6. Show marks for a course")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()