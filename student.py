class Student:

    def __init__(self, lname, fname, id, courses=[]):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.courses = []
        for c in courses:
            self.addCourse(c)

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
