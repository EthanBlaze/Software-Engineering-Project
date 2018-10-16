class Teacher:
    def __init__(self, lname, fname, password):
        self.lname = lname
        self.fname = fname
        self.password = password


    def ___str___(self):
        return f"Teacher: {self.lname}, {self.fname}"

    def __repr__(self):
        return f"Teacher({self.lname}, {self.fname}, {self.password}"
