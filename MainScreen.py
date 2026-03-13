from tkinter import *

import PlayerForm
import VolunteerForm
import AdminPage
import AdminLogin
import Database

'''
Class MainScreen handles the creation of the main menu that everyone sees.
It is the first screen seen on startup and all other windows will eventually
lead back to it.
'''
class MainScreen:
    # Method that makes sure program halts after closing window
    def quit(self):
        self.mainScreen.quit()
        self.mainScreen.destroy()


    # Create instances of the classes
    playerScreen = PlayerForm.PlayerForm()
    volunteerScreen = VolunteerForm.VolunteerForm()
    adminLogin = AdminLogin.AdminLogin()
    database = Database.Database()

    # Create the Database
    database.createDatabase()

    def adminButtonClicked(self):
        self.mainScreen.withdraw()
        self.adminLogin.createAdminLogin()

    '''
    createMainScreen will make the main menu for the program.
    As long as registration is still open, it will display both registration
    buttons.  When an admin closes registration, those buttons will be replaced
    with a button to view the bracket.
    '''
    def createMainScreen(self):

        #If admin has closed registration, do not show those buttons
        if (AdminPage.regClosed):
            # Create the main screen
            self.mainScreen = Tk(className='Tournament Manager')
            self.mainScreen.protocol("WM_DELETE_WINDOW", quit)
            self.mainScreen.geometry("800x600")
            self.mainScreen.deiconify()
            closedLabel = Label(self.mainScreen, text="Registration is now closed.", width=30, height=8).pack()
            adminButton = Button(self.mainScreen, text='Admin Login', width=30, height=8, bg='#0052cc', fg='#ffffff', \
                                 font=20, command=self.adminButtonClicked).pack()
            bracketButton = Button(self.mainScreen, text='View Bracket', width=30, height=8, bg='#0052cc', fg='#ffffff', \
                                 font=20).pack()

        #If registration is still open
        else:
            self.mainScreen = Tk(className='Tournament Manager')
            self.mainScreen.protocol("WM_DELETE_WINDOW", quit)
            self.mainScreen.geometry("800x600")
            # Buttons for forms
            playerButton = Button(self.mainScreen, text='Player Registration', width=30, height=8, bg='#0052cc', fg='#ffffff', \
                                  font=20, command=self.playerScreen.createPlayerForm).pack()
            volunteerButton = Button(self.mainScreen, text='Volunteer Registration', width=30, height=8, bg='#0052cc',
                                     fg='#ffffff', \
                                     font=20, command=self.volunteerScreen.createVolunteerForm).pack()
            adminButton = Button(self.mainScreen, text='Admin Login', width=30, height=8, bg='#0052cc', fg='#ffffff', \
                                 font=20, command=self.adminButtonClicked).pack()

        self.mainScreen.mainloop()