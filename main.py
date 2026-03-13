import sqlite3
from tkinter import *

import PlayerForm
import VolunteerForm
import AdminPage
import AdminLogin
import Database
import MainScreen


'''
Main Method:
Creates the screen seen on startup
If registration is open, buttons for players and volunteers to register will show
If registration is closed, a button to view the bracket will show
Admin login will always show
'''
def main():

    mainScreen = MainScreen.MainScreen()
    mainScreen.createMainScreen()





    '''
    #Method that makes sure program halts after closing window
    def quit():
        mainScreen.quit()
        mainScreen.destroy()

    #Create instances of the classes
    playerScreen = PlayerForm.PlayerForm()
    volunteerScreen = VolunteerForm.VolunteerForm()
    adminLogin = AdminLogin.AdminLogin()
    database = Database.Database()

    #Create the Database
    database.createDatabase()

    #Create the main screen
    mainScreen = Tk(className='Tournament Manager')
    mainScreen.protocol("WM_DELETE_WINDOW", quit)
    mainScreen.geometry("800x600")

    def adminButtonClicked():
        mainScreen.withdraw()
        adminLogin.createAdminLogin()

    if(AdminPage.regClosed):
        closedLabel = Label(mainScreen, "Registration is now closed.").pack()
        adminButton = Button(mainScreen, text='Admin Login', width=30, height=8, bg='#0052cc', fg='#ffffff', \
                             font=20, command=adminLogin.createAdminLogin).pack()
    else:
        #Buttons for forms
        playerButton = Button(mainScreen, text='Player Registration', width=30, height=8, bg='#0052cc', fg='#ffffff',\
                              font=20, command=playerScreen.createPlayerForm).pack()
        volunteerButton = Button(mainScreen, text='Volunteer Registration', width=30, height=8,bg='#0052cc',fg='#ffffff', \
                              font=20, command=volunteerScreen.createVolunteerForm).pack()
        adminButton = Button(mainScreen, text='Admin Login', width=30, height=8, bg='#0052cc', fg='#ffffff', \
                             font=20, command=adminButtonClicked).pack()

    mainScreen.mainloop()
    '''


# Execute the main function.
if __name__ == '__main__':
    main()
