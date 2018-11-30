import tkinter as tk
from tkinter import ttk
import pickle
import bisect
from tkinter import messagebox as msg
from student import Student
from teacher import Teacher
from course import Course

FONT = ("Times New Roman", 16)
currentUser = None

# Opening students.dat to populate students[] -- if this throws an error for you, run initialize_data.py to fix it
with open("students.dat", "rb") as fp:
    students = pickle.load(fp)

# Opening teachers.dat to populate teachers[]
with open("teachers.dat", "rb") as fp:
    teachers = pickle.load(fp)

courses=[]

for student in students:
    for course in student.courses:
        if course.title not in courses:
            bisect.insort(courses, course.title)

print(courses)


class Bookworm(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        # tk.Tk.iconbitmap(self, default="hex.ico")
        tk.Tk.wm_title(self, "Bookworm LMS")

        # container.pack(side="top", fill = "both", expand=True)
        container.grid(row=0, column =0)
        #
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Add frames listed in tuple to self.frames{}
        for F in (Login, TeacherGUI, StudentGUI):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(TeacherGUI)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def loginaction(name, passwd):
    user_info = [name, passwd]
    print(user_info)
    for t in teachers:
        if name == t.lname:
            if passwd == t.password:
                currentUser = t
                return
    for s in students:
        if name == s.fname:
            if passwd == s.id:
                currentUser = s
                return
    msgwin = msg.showinfo("Login Error", "Username/password invalid. Try again.")


def teacher_login(name, passw):
    user_info = [name, passw]
    win = tk.Tk()
    win.title("Welcome to the Teacher Portal")
    user = tk.Label(text=user_info[0])

    password = tk.Label(text=user_info[1])


class Login(tk.Frame):

    def buttonSLogin(self):
        print(student_username.get())

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label
        # title = tk.Label(text="Hello, Please enter your login information.", font=FONT)
        # title.grid(column=0, row=0)


        studentname = tk.StringVar()
        studentpass = tk.StringVar()
        student_username = ttk.Entry(self, width=20, textvariable=studentname)
        student_password = ttk.Entry(self, width=20, textvariable=studentpass)
        student_pass = ttk.Entry()
        student_username.grid(column=0, row = 1)
        student_password.grid(column=0, row =2)

        student_button = tk.Button(text="Login", command = lambda : loginaction(student_username.get(),
                                                                                             student_password.get()))
        # teacher_button = tk.Button(text = "Login as Teacher")
        student_button.grid(column = 0, row = 3)
        # teacher_button.pack()


class TeacherGUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tabbedControl = ttk.Notebook(self)

        for c in courses:
             temp_tab = ttk.Frame(tabbedControl)
             tabbedControl.add(temp_tab, text=c)
             tabbedControl.pack(expand=1, fill='both')

        for s in students:
            student_info = str(s)
            label = ttk.Label(temp_tab, text = student_info)
            label.pack()




class StudentGUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page Two", font = FONT)

        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button1 = ttk.Button(self, text="Back to Page One", command=lambda: controller.show_frame(PageOne))
        button1.pack()


app = Bookworm()
app.mainloop()

