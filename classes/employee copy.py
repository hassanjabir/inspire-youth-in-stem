#!/usr/bin/python

#####################
#   gui_operations
#   Jabir Hassan
#   date: 2/6/2022
#####################


from tkinter import *

window = Tk()
window.title("hi welcome to this fantstic application")
window.configure(bg="blue")
window.geometry("900*700")
f_name = Label(window , text ="First name", font = ("aerial bold",20))
s_name = Label(window, text = "second name", font = ("aerial bold",20))
f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 100)
window.mainloop
