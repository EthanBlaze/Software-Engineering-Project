import tkinter as tk


window = tk.Tk()
window.title("Student/Teacher Login")
window.geometry("400x400")

# Label
title = tk.Label(text= "Hello, Please enter your login information.", font = ("Times New Roman", 12))
title.grid(column =1, row= 0)
StudentTitle = tk.Label(text = "Student Login", font= ("Times New Roman", 13))
StudentTitle.grid(column=1, row = 2)
Username = tk.Label(text= "Username")
Username.grid(column =0, row = 3)
Password = tk.Label(text = "Password")
Password.grid(column= 0, row= 4)
# Button
button1 = tk.Button(text ="Login", bg="red")
button1.grid(column=1, row =5)

#Entry Field
Username_Entry_Field = tk.Entry()
Username_Entry_Field.grid(column = 1, row = 3)
Password_Entry_Field =tk.Entry()
Password_Entry_Field.grid(column= 1, row =4)

#Teacher Login
StudentTitle = tk.Label(text = "Teacher Login", font= ("Times New Roman", 13))
StudentTitle.grid(column=1, row = 7)
Username = tk.Label(text= "Username")
Username.grid(column =0, row = 8)
Password = tk.Label(text = "Password")
Password.grid(column= 0, row= 9)

#Teacher EntryField
Username_Entry_Field = tk.Entry()
Username_Entry_Field.grid(column = 1, row = 8)
Password_Entry_Field =tk.Entry()
Password_Entry_Field.grid(column = 1, row =9)
# Teacher Button
button1 = tk.Button(text ="Login", bg= "light blue")
button1.grid(column=1, row =10)

#Photo Icon
photo = tk.PhotoImage(file = "Login_Photo.png")
photoLabel = tk.Label(window, image = photo)
photoLabel.grid(column = 1, row = 1)

window.mainloop()

