import pickle

teachers = []
temp = Teacher('queen', 'heather', "admin")
teachers.append(temp)
temp = Teacher('gryphon', 'riley', "abc123")
teachers.append(temp)

students = []
temp = Student('treacle', "elsie", "0001")
students.append(temp)
temp = Student('treacle', 'lacie', "0002")
students.append(temp)
temp = Student('treacle', 'tillie', "0003")
students.append(temp)
temp = Student('liddell', 'alice', "0004")
students.append(temp)
temp = Student('red', 'prickett', '0005')
students.append(temp)
temp = Student('liddell', 'lory', '0006')
students.append(temp)
temp = Student('hatta', 'tarrant', '0007')
students.append(temp)
temp = Student('hare', 'haigha', "0008")
students.append(temp)

# SAVING TEACHERS[] TO teachers.dat
with open("teachers.dat", "wb") as fp:
    pickle.dump(teachers, fp)

# SAVE STUDENTS[] TO students.dat
with open("students.dat", "rb") as fp:
    students = pickle.load(fp)
