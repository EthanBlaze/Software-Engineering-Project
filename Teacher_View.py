import tkinter as tk
from tkinter import ttk
from student import *
from tkinter import scrolledtext
window = tk.Tk()
window.title("Teacher Login Page")
window.geometry("500x500")

# Label
title = tk.Label(window,text= "What would you like to do?", font = ("Times New Roman", 12))
title.grid(column =2, row= 0)

ttk.Label(window, text = "What class would you like to view? ", font = ("Times New Roman",12)).grid(column =2, row =1)
Stud_Courses= tk.StringVar()
Courses= tk.StringVar()
Courses_chosen = ttk.Combobox(window, width =12, textvariable = Courses)
Courses_chosen['values']= ("Bio1", "Math1", "EngLit", "Chess1")
Courses_chosen.grid(column = 2, row= 2)
Courses_chosen.current(0)


def Input_student_id():
    scr.configure(text ="Please enter student ID.")


addGrades = ttk.Button(window, text="Add Grades", )
addGrades.grid(column=2, row=5)

Find_stud = ttk.Button(window, text="Find Students",command = Input_student_id)
Find_stud.grid(column=2, row=4)

#scroll textbox
scroll_width = 30
scroll_height = 20
scr = scrolledtext.ScrolledText(window, width = scroll_width, height = scroll_height, wrap = tk.WORD)
scr.grid(column = 3, row =5)



window.mainloop()

