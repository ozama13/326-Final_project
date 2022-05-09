#test 
#import module
from tkinter import *
import musicshare
import song
import user

#creating root window
root = Tk()

#root window title and dimension
root.title("Welcome to Music Share!")
#Set geometry (widthxheight)
root.geometry('750x250')

#setting up Tkinter frame
def display_text():
    username = user_name.get()
    Label(ws, text=f'Welcome,{username},!',pady=20).pack()

 #enter button to move to next window
 user_name= Entry(ws)
 username.pack(pady=30)

#creating next window for playlist entry

Button(
    ws,
    text = "Enter"
    padx=10
    pady=5
    command=display_text
).pack()
#next window
ws.mainloop()

root.configure(background='grey')

#simple form to create playlist using user input

playlist_entry = Label(root, text="Input your selected songs:")
genre_menu = StringVar(root)
genre= OptionMenu(root, genre_menu,
    'Rap',
    'Country',
    'Pop',
    'EDM',
    'Rock',
    'Soul',
    'Funk').grid(row=0, column=0)
genre.pack()
artist = Label(root, text='Artist Name').grid(row=1, column=0)
song = Label(root, text='Song Title').grid(row=2, column=0)
a1= Entry(root).grif(row=0,column=1)
a2= Entry(root).grif(row=1,column=1)
a3= Entry(root).grif(row=2,column=1)

#after user entry

def clicked():
    res='Hold on, we are generating a shared playlist'+txt.get()

btn= Button(root, text="Submit").grid(row=4, column=0)



def findFriend(friendUsername):
    """opens file of user objects and returns the playlist of the corresponding friend

    Args:
        friendUsername (string): string of the username of friend wanted to add to connect to
    """
    user_data = open(r"user_database","a")
    for line in findFriend:
        line.split()
        if friendUsername == line[0]:
            pass

    user_data.close()



