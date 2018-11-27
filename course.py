class Course:
    def __init__(self, title):
        self.title = title
        self.grades = []
        self.gpa = ' '

    def addGrade(self, score):
        self.grades.append(score)
        self.calcGPA()

    def getTitle(self):
        return self.title

    def calcGPA(self):
        """
        Adjusts the GPA of the student based on values in grades[]
        This function is automatically called by addGrade() each time a grade is added to update the GPA
        :return:
        """
        if self.grades:
            average = sum(self.grades) / (len(self.grades))
            if average >= 90.0:
                self.gpa = '4.0'
            elif average >= 80.0:
                self.gpa = '3.0'
            elif average >= 70.0:
                self.gpa = '2.0'
            elif average >= 60.0:
                self.gpa = '1.0'
            else:
                self.gpa = '0.0'

    def __str__(self):
        """
        Return the string representation of the course: its title, a list of all grades for this course, and GPA
        :param self:
        :return:
        """
        string = f"{self.title}"
        if self.grades:
            string += "\tGrades: " + str(self.grades)
            string += f" Resulting GPA: {self.gpa}"
        return string