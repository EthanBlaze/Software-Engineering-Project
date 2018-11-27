from inputErrors import NameWithNumbersError
from inputErrors import NoNameError
 
 
 class Student:

	def __init__(self, lname, fname, id, courses=[]):
        self.fname = fname
        self.lname = lname
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
        self.courses = []
        for course in courses:
            self.addCourse(course)
    
	def addCourse(self, course):
        self.courses.append(course)