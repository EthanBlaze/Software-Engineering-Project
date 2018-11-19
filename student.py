from inputErrors import NameWithNumbersError
from inputErrors import NoNameError


class Student:

    def __init__(self, lname, fname, id, courses=[]):
        try:
            if any(str.isdigit(c) for c in lname) or any(str.isdigit(c) for c in fname):
                raise NameWithNumbersError
            elif not lname or not fname:
                raise NoNameError
            else:
                self.fname = fname
                self.lname = lname
        except NameWithNumbersError:
            return "Name cannot contain anything other than letters."
        except NoNameError:
            return "Names cannot be blank."
        self.id = id
        for course in courses:
            self.addCourse(course)

    def addCourse(self, course):
        self.courses.append(course)

    def __str__(self):
        """Returns string showing lastname, firstname, studentID, courses, grades, and gpa"""
        profile = (f"{self.lname.title()}, {self.fname.title()} -- Student ID: {self.id}\n"
                   f"Enrolled in: \n")
        for course in self.courses:
            profile += f"\t{str(course)}\n"
        return profile

    def __repr__(self):
        return f"Student({self.lname},{self.fname},{self.id}, {self.courses})"
