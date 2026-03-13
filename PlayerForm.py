from tkinter import *
import sqlite3

"""
class PlayerForm contains methods to create the player registration GUI
and stores the user's information in the database.
"""
class PlayerForm:


    '''
    submitPlayerForm is called when the submit button in the
    registration form is clicked.  Entered information is
    stored in variables, then sent to the database.
    '''
    def submitPlayerForm(self):

        #Store entered info in variables
        name = self.nameEntry.get()
        phone = self.phoneEntry.get()
        email = self.emailEntry.get()
        if(self.genderVar.get() == 1):
            gender = "Male"
        else:
            gender = "Female"

        # Open database connection
        conn = sqlite3.connect('tournament.db')
        cur = conn.cursor()

        #insert entered info into database
        cur.execute('''INSERT INTO Player(name, phone, email, gender) VALUES (?,?,?,?)''',\
                        (name, phone, email, gender))

        #Commit changes and close connection
        conn.commit()
        conn.close()



    #Components for Player form
    playerWindow = Tk()
    playerWindow.title("Player Registration")
    playerWindow.withdraw()

    playerTitleLabel = Label(playerWindow, text="Player Registration", font=('Arial 24 bold'))

    playerNameLabel = Label(playerWindow, text='Name')
    nameEntry = Entry(playerWindow)

    playerPhoneLabel = Label(playerWindow, text='Phone Number')
    phoneEntry = Entry(playerWindow)

    playerEmailLabel = Label(playerWindow, text='Email')
    emailEntry = Entry(playerWindow)

    playerGenderLabel = Label(playerWindow, text='Gender:')
    genderVar = IntVar()
    maleButton = Radiobutton(playerWindow, text='Male', variable = genderVar, value=1)
    femaleButton = Radiobutton(playerWindow, text='Female', variable=genderVar, value=2)


    '''
    Method to create player form
    Shows the window and places all components on window
    '''
    def createPlayerForm(self):
        self.playerWindow.deiconify()
        self.playerTitleLabel.grid(row=0)
        self.playerNameLabel.grid(row=1)
        self.nameEntry.grid(row=1, column=1)

        self.playerPhoneLabel.grid(row=2)
        self.phoneEntry.grid(row=2, column=1)

        self.playerEmailLabel.grid(row=3)
        self.emailEntry.grid(row=3, column=1)

        self.maleButton.grid(row=4)
        self.femaleButton.grid(row=5)

        #Button calls submitPlayerForm method on click
        submitButton = Button(self.playerWindow, text='Submit', command=self.submitPlayerForm)
        submitButton.grid(row=7)

