from tkinter import *

import MainScreen

regClosed = False

class AdminPage:

    adminWindow = Tk()
    adminWindow.title("Admin")
    adminWindow.geometry("600x600")
    adminWindow.withdraw()

    adminTitleLabel = Label(adminWindow, text="Admin Page", font=('Arial 24 bold')).grid(row=0)

    def closeRegClicked(self):
        global regClosed
        regClosed = True
        main2 = MainScreen.MainScreen()
        main2.createMainScreen()


    def createAdminWindow(self):
        self.adminWindow.deiconify()
        #Create buttons for closing registration and create bracket
        closeRegButton = Button(self.adminWindow, text='Close Registration',width=30, height=8, bg='#0052cc', fg='#ffffff',\
                              font=20, command=self.closeRegClicked)
        createBracketButton = Button(self.adminWindow, text='Create Bracket',width=30, height=8, bg='#0052cc', fg='#ffffff',\
                              font=20)

        closeRegButton.grid(row=1)
        createBracketButton.grid(row=2)