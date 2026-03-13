import sqlite3

"""
class Database is responsible for creating the 
database and all tables within. 
"""
class Database:

    '''
    createDatabase is called in the main method to create the database
    on the first run.  If the tables have already been created,
    this method will not do anything.
    '''
    def createDatabase(self):
        conn = sqlite3.connect('tournament.db')
        cur = conn.cursor()

        #Create Player table
        cur.execute('''CREATE TABLE IF NOT EXISTS Player (
                        id INTEGER PRIMARY KEY,
                        name TEXT, 
                        phone TEXT,
                        email TEXT,
                        gender TEXT
                        );''')
        #Create Volunteer table
        cur.execute('''CREATE TABLE IF NOT EXISTS Volunteer (
                                id INTEGER PRIMARY KEY,
                                name TEXT, 
                                phone TEXT,
                                email TEXT,
                                gender TEXT,
                                hoursAvail INT
                                );''')
        #Create admin table
        cur.execute('''CREATE TABLE IF NOT EXISTS Admin (
                                        id INTEGER PRIMARY KEY,
                                        username TEXT, 
                                        password TEXT
                                        );''')
        #Commit changes and close connection
        conn.commit()
        conn.close()
