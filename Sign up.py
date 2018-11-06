import pymysql
from pyqt5 import *

def Signup():  # This is the signup definition,
    global pwordE
    global nameE
    global roots

    roots = Tk()  # This creates the window, just a blank one.
    roots.title('SignUp')  # This renames the title of said window to 'signup'
    intruction = Label(roots,
                       text='Please Enter New Username & Password\n')
    intruction.grid(row=0, column=0,
                    sticky=E)

    nameL = Label(roots, text='New Username: ')  # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ')
    nameL.grid(row=1, column=0,
               sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)

    nameE = Entry(roots)  # This now puts a text box waiting for input.
    pwordE = Entry(roots,
                   show='*')
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)

    signupButton = Button(roots, text='SignUp',
