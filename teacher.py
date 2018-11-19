from inputErrors import NameWithNumbersError
from inputErrors import NoNameError


class Teacher:
    def __init__(self, lname, fname, password):
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
        self.password = password


    def ___str___(self):
        return f"Teacher: {self.lname}, {self.fname}"

    def __repr__(self):
        return f"Teacher({self.lname}, {self.fname}, {self.password}"
