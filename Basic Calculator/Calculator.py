from tkinter import *

root = Tk()
root.title("Mouad Calculator")
root.configure(bg="gray27")
e = Entry(root, width=15, borderwidth=14,fg="white", font=("calibri", 30), bg="gray45")
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

#Button functions

def Button_Click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def Button_clear():
    e.delete(0, END)
def Button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def Button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)    
def Button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

#Buttons definitions

Button_1 = Button(root, borderwidth=9, text="1",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(1))
Button_2 = Button(root, borderwidth=9, text="2",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(2))
Button_3 = Button(root, borderwidth=9, text="3",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(3))
Button_4 = Button(root, borderwidth=9, text="4",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(4))
Button_5 = Button(root, borderwidth=9, text="5",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(5))
Button_6 = Button(root, borderwidth=9, text="6",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(6))
Button_7 = Button(root, borderwidth=9, text="7",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(7))
Button_8 = Button(root, borderwidth=9, text="8",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(8))
Button_9 = Button(root, borderwidth=9, text="9",fg="white", font=("calibri", 15), bg="gray45", padx=39, pady=15, command=lambda: Button_Click(9))
Button_0 = Button(root, borderwidth=9, text="0",fg="white", font=("calibri", 15), bg="gray45", padx=96, pady=15, command=lambda: Button_Click(0))

Button_add = Button(root, borderwidth=7, text="+",fg="white", font=("calibri", 15), bg="gray47", padx=20, pady=7, command=Button_add)
Button_subtract = Button(root, borderwidth=7, text="-",fg="white", font=("calibri", 15), bg="gray47", padx=20, pady=7, command=Button_subtract)
Button_clear = Button(root, borderwidth=7, text="Clear",fg="white", font=("calibri", 15), bg="gray47", padx=20, pady=7, command =Button_clear)
Button_equal = Button(root, borderwidth=7, text="=",fg="white", font=("calibri", 15), bg="gray30", padx=41, pady=15, command=Button_equal)

#Bottuns on  the screen

Button_add.grid(row=1, column=0)
Button_subtract.grid(row=1, column=1)
Button_clear.grid(row=1, column=2)
Button_equal.grid(row=5, column=2)

Button_1.grid(row=4, column=0)
Button_2.grid(row=4, column=1)
Button_3.grid(row=4, column=2)

Button_4.grid(row=3, column=0)
Button_5.grid(row=3, column=1)
Button_6.grid(row=3, column=2)

Button_7.grid(row=2, column=0)
Button_8.grid(row=2, column=1)
Button_9.grid(row=2, column=2)

Button_0.grid(row=5, columnspan=2)



root.mainloop()