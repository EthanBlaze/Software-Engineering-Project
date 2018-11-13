import tkinter as tk
from tkinter import ttk
from student import *
from tkinter import scrolledtext
window = tk.Tk()
window.title(" Student ViewPage")
window.geometry("500x500")

# Label


ttk.Label(window, text = "What class would you like to view? ", font = ("Times New Roman",12)).grid(column =2, row =1)
Stud_Courses= tk.StringVar()
Courses= tk.StringVar()
Courses_chosen = ttk.Combobox(window, width =12, textvariable = Courses)
Courses_chosen['values']= ("Bio1", "Math1", "EngLit", "Chess1")
Courses_chosen.grid(column = 2, row= 2)
Courses_chosen.current(0)





addCourses = ttk.Button(window, text="Add Courses", )
addCourses.grid(column=2, row=5)

view_grade = ttk.Button(window, text="View Grades")
view_grade.grid(column=2, row=4)

#scroll textbox
scroll_width = 30
scroll_height = 20
scr = scrolledtext.ScrolledText(window, width = scroll_width, height = scroll_height, wrap = tk.WORD)
scr.grid(column = 3, row =5)



window.mainloop()

