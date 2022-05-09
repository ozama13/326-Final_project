#test 
#import module
from tkinter import *
import musicshare
import song
import user


def main_account_screen():
    #creating root window
    main_account = Tk()   
    #root window title and dimension
    main_account.title("Welcome to Music Share!")
    #Set geometry (widthxheight)
    main_account.geometry('750x250')

#setting up labels for user input
    Label(text="Login or Signup", bg='papayawhip',width=300, height='2',font=('Arial',14)).pack()
    Label(text='').pack()

#creating login button
    Button(text="Login",height='2', width='30').pack()
#creating signup button
    Button(text='Register', height='2',width='30').pack()

#start GUI
    main_account_screen.mainloop()
#call main_account_screen
    main_account_screen()

#signup window:
def signup():
    signup_screen= Toplevel(main_screen)
    signup_screen.title('Signup')
    signup_screen.geometry('300x250')
#text variables
    username=StringVar()
    password=StringVar()
#labels for signup instructions
    Label(signup_screen, text="Please enter your information below", bg='papayawhip').pack()
    Label(signup_screen, text='').pack()
    username_lable = Label(signup_screen, text="Username * ")
    username_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    username_entry = Entry(signup_screen, textvariable=username)
    username_entry.pack()
   
# Set password label
    password_lable = Label(signup_screen, text="Password * ")
    password_lable.pack()
    
# Set password entry
    password_entry = Entry(signup_screen, textvariable=password, show='*')
    password_entry.pack()

#set email entry
    email_entry = Entry(signup_screen, textvariable=email, show='*')
    email_entry.pack()

#set email label
    email_lable = Label(signup_screen, text="Email * ")
    email_lable.pack()



    Label(signup_screen, text="").pack()
    
# Set signup button
    Button(signup_screen, text="Signup", width=10, height=1, bg="papayawhip").pack()

global main_screen

#signup button
Button(text='Signup', height='2',width='30',command=Signup).pack()

#simple form to create playlist using user input

playlist_entry = Label(main_account, text="Input your selected songs:")
genre_menu = StringVar(main_account)
genre= OptionMenu(root, genre_menu,
    'Rap',
    'Country',
    'Pop',
    'EDM',
    'Rock',
    'Soul',
    'Funk').grid(row=0, column=0)
genre.pack()
artist = Label(main_account, text='Artist Name').grid(row=1, column=0)
song = Label(main_account, text='Song Title').grid(row=2, column=0)
a1= Entry(main_account).grif(row=0,column=1)
a2= Entry(main_account).grif(row=1,column=1)
a3= Entry(main_account).grif(row=2,column=1)

#after user entry

def clicked():
    #res='Hold on, we are generating a shared playlist'+txt.get()

btn= Button(main_account, text="Submit").grid(row=4, column=0)



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



