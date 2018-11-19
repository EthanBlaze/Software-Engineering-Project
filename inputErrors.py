class Error(Exception):
    """Base class for other exceptions"""
    pass


class GradeNegativeError(Error):
    """Raised when the grade input is negative"""
    pass


class GradeTooLargeError(Error):
    """Raised when the grade input is larger than 120"""
    pass


class GradeNotDigitError(Error):
    """Raised when the grade input contains anything other than a number"""
    pass


class NameWithNumbersError(Error):
    """Raised when name contains any digits"""
    pass
	

class NoNameError(Error):
	"""Raised when name is an empty string"""
	pass