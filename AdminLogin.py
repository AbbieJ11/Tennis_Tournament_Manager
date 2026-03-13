import tkinter.messagebox
from tkinter import *
import sqlite3
import AdminPage

"""
class AdminLogin contains methods for creating the admin login page GUI
and handles authentication of the user's username and password from
the database.
"""
class AdminLogin:

    '''
    submitAdminLogin method is called when the submit button is clicked
    in the admin form.  It stores the info the user entered, then compares
    it to already stored user/pass combinations in the database.  If they
    match, the admin screen will appear.  If they don't match, an error
    message will appear and tell the user to try again.
    '''
    def submitAdminLogin(self):

        #Store the entered username and password
        username = self.userEntry.get()
        password = self.passEntry.get()
        #Store the combination of username and password together
        login = (username, password)

        # Open database connection
        conn = sqlite3.connect('tournament.db')
        cur = conn.cursor()

        # Retrieve list of stored usernames and passwords
        cur.execute("SELECT username, password FROM Admin")
        rows = cur.fetchall()

        #variable to store login success
        success = False

        # See if any user/pass combinations in database match what user entered
        #Loop through rows in database using (username, password) combinations
        for row in rows:
            #If the user/pass match
            if login == row:
                print("Success")
                #Login is correct; no need to keep comparing so break
                success = True
                break

        #If there were no matches, display an error message
        if success == False:
            tkinter.messagebox.showinfo("Invalid Login", "The username or password is incorrect.  Please try again.")
        #If there was a match
        else:
            #open the admin page.
            self.adminWindow.withdraw()
            adminPage = AdminPage.AdminPage()
            adminPage.createAdminWindow()



        #Commit changes and close connection
        conn.commit()
        conn.close()



    #Create the window and hide until the create method is called
    adminWindow = Tk()
    adminWindow.title("Admin Login")
    adminWindow.withdraw()

    #Create components
    titleLabel = Label(adminWindow, text="Admin Login", font=('Arial 24 bold'))
    adminUserLabel = Label(adminWindow, text="Username")
    userEntry = Entry(adminWindow)
    adminPassLabel = Label(adminWindow, text="Password")
    passEntry = Entry(adminWindow)


    '''
    method createAdminLogin places all components on the adminLogin window and shows the window.
    It is called from the main method when the admin login button is clicked.
    '''
    def createAdminLogin(self):
        self.adminWindow.deiconify()
        self.titleLabel.grid(row=0)
        self.adminUserLabel.grid(row=1)
        self.userEntry.grid(row=1, column=1)
        self.adminPassLabel.grid(row=2)
        self.passEntry.grid(row=2, column=1)

        #Submit button calls submitAdminLogin method when clicked
        submitButton = Button(self.adminWindow, text='Submit', command=self.submitAdminLogin).grid(row=3)