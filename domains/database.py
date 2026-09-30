import math
import numpy

students = []
courses = []
marks = {}

def round_down_mark(mark):
    return math.floor(mark*10)/10

def calculate_gpa():
    for student in students:
        student_marks = []
        student_credits = []

        for course in courses:
            course_id = course['id']
            if course_id in marks and student['id'] in marks[course_id]:
                student_marks.append(marks[course_id][student['id']])
                student_credits.append(course['credits'])

            if student_marks:
                numpy_marks = numpy.array(student_marks)
                numpy_credits = numpy.array(student_credits)

                gpa = numpy.sum(numpy_marks*numpy_credits)/ numpy.sum(numpy_credits)
                student['gpa'] = round_down_mark(gpa)
            else:
                student['gpa'] = 0.0