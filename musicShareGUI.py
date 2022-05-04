#test 
# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Welcome to Music Share!")
# Set geometry(widthxheight)
root.geometry('350x200')
 
# adding a label to the root window
lbl = Label(root, text = "Playlist recommender based on your friend's playlist")
lbl.grid()
 
# function to display text when
# button is clicked
def clicked():
    lbl.configure(text = "Hold on, your playlist is being created.")
 
# button widget with red color text
# inside
btn = Button(root, text = "Start" ,
             fg = "blue", command=clicked)
# set Button grid
btn.grid(column=1, row=0)