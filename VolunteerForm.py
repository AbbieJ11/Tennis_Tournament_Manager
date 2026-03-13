from tkinter import *
import sqlite3

"""
class VolunteerForm handles creation of volunteer registration GUI
and stores entered info in the database.
"""
class VolunteerForm:

    # submitVolunteerForm is called when the submit button in the
    # registration form is clicked.  Entered information is
    # stored in variables, then sent to the database.
    def submitVolunteerForm(self):
        name = self.nameEntry.get()
        phone = self.phoneEntry.get()
        email = self.emailEntry.get()
        if (self.genderVar.get() == 1):
            gender = "Male"
        else:
            gender = "Female"
        hoursAvailable = self.hoursEntry.get()

        # Open database connection
        conn = sqlite3.connect('tournament.db')
        cur = conn.cursor()

        # insert entered info into database
        cur.execute('''INSERT INTO Volunteer(name, phone, email, gender, hoursAvail) VALUES (?,?,?,?,?)''', \
                    (name, phone, email, gender, hoursAvailable))

        #Commit changes and close connection
        conn.commit()
        conn.close()

    # Components for Volunteer form
    volunteerWindow = Tk()
    volunteerWindow.title("Volunteer Registration")
    volunteerWindow.withdraw()

    volunteerTitleLabel = Label(volunteerWindow, text="Volunteer Registration", font=('Arial 24 bold'))

    volunteerNameLabel = Label(volunteerWindow, text='Name')
    nameEntry = Entry(volunteerWindow)

    volunteerPhoneLabel = Label(volunteerWindow, text='Phone Number')
    phoneEntry = Entry(volunteerWindow)

    volunteerEmailLabel = Label(volunteerWindow, text='Email')
    emailEntry = Entry(volunteerWindow)

    volunteerGenderLabel = Label(volunteerWindow, text='Gender:')
    genderVar = IntVar()
    maleButton = Radiobutton(volunteerWindow, text='Male', variable=genderVar, value=1)
    femaleButton = Radiobutton(volunteerWindow, text='Female', variable=genderVar, value=2)

    volunteerHourLabel = Label(volunteerWindow, text='Hours Available:')
    hoursEntry = Entry(volunteerWindow)

    # Method to create player form
    # Shows the window and places all components on window
    def createVolunteerForm(self):
        self.volunteerWindow.deiconify()
        self.volunteerTitleLabel.grid(row=0)
        self.volunteerNameLabel.grid(row=1)
        self.nameEntry.grid(row=1, column=1)

        self.volunteerPhoneLabel.grid(row=2)
        self.phoneEntry.grid(row=2, column=1)

        self.volunteerEmailLabel.grid(row=3)
        self.emailEntry.grid(row=3, column=1)

        self.maleButton.grid(row=4)
        self.femaleButton.grid(row=5)

        self.volunteerHourLabel.grid(row=6)
        self.hoursEntry.grid(row=7)

        #Submit button calls submitVolunteerForm on click
        submitButton = Button(self.volunteerWindow, text='Submit', command=self.submitVolunteerForm)
        submitButton.grid(row=8)