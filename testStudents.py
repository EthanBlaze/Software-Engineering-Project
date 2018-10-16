from student import Student
from course import Course
from teacher import Teacher
import bisect
import pickle

# Opening students.dat to populate students[] -- if this throws an error for you, run initialize_data.py to fix it
with open("students.dat", "rb") as fp:
    students = pickle.load(fp)

# Opening teachers.dat to populate teachers[]
with open("teachers.dat", "rb") as fp:
    teachers = pickle.load(fp)


logged_in = students[6]
print(logged_in.fname)

logged_in.addCourse(Course("Bio1"))
logged_in.addCourse(Course("Math1"))
logged_in.addCourse(Course("Chess1"))
students[5].addCourse(Course("Bio1"))
students[1].addCourse(Course("Bio1"))
students[4].addCourse(Course("EngLit"))
courses = []
courseSeeking = "Bio1"
enrolled = []
for student in students:
    for course in student.courses:
        if course.title not in courses:
            bisect.insort(courses, course.title)
        if course.title == courseSeeking:
            enrolled.append(f"{student.lname.title()}, {student.fname.title()}")
print("Students enrolled in " + courseSeeking + ": " + str(enrolled))
print(courses)

# PRINTING ALL COURSES LOGGED-IN STUDENT IS ENROLLED IN
# for courses in logged_in.courses:
#     print(courses.title)

# ADDING A GRADE TO A COURSE FOR A LOGGED-IN STUDENT
# gradeToAdd = 88
# inCourse = "Chess1"
# index = next(x for x in logged_in.courses if x.title == inCourse)
# index.addGrade(gradeToAdd)
# index.addGrade(93)
#
# print(logged_in)

# SEARCH STUDENTS FOR A PROPERTY
# madHatter = next(x for x in students if x.id == "0007")
# print(madHatter.lname)
#
# SAVE STUDENTS[] TO students.dat
# with open("students.dat", "rb") as fp:
#     students = pickle.load(fp)
#
# GETTING CURRENT USER'S INFO  -- ALREADY DEPRECATED WITH __str__ ADDITION
# currentuser = "0002"
# for item in students:
#     if item.id == currentuser:
#         print(item.fname, item.lname, item.id, item.gpa)
#         print(item.classes)
#
# SAVING TEACHERS[] TO teachers.dat
# with open("teachers.dat", "wb") as fp:
#       pickle.dump(teachers, fp)
