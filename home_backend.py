import sqlite3 
from datetime import datetime,timedelta


def connect():
    '''
    A function to create connection with database and create a cursor.
    It also checks whether there is a table present if not it creates a new one.
    '''
    conn= sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS note(date text, spotting text, fluid text, sex text, temperature integer, pain text, pill text, mood text)")
    conn.commit()
    conn.close()

def insert(date,spotting,fluid,sex,temperature,pain,pill,mood):
    """
    This function helps to insert the data into the database.
    """
    conn= sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO note VALUES (?,?,?,?,?,?,?,?)",(date,spotting,fluid,sex,temperature,pain,pill,mood))

    conn.commit()
    conn.close()

def view():
    """
    This function allows to retrieve all the data from the table of the database.
    Returns rows as a tuple 
    """
    conn= sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM note")
    rows = cur.fetchall()
    conn.close()
    return rows

# TO WORK
def search(date):
    conn= sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM note WHERE date=?", (date,))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(date):
    conn= sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM note WHERE date=?",(date,))
    conn.commit()
    conn.close()

def update(date,spotting,fluid,sex,temperature,pain,pill,mood):
    conn= sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute("UPDATE note SET spotting=?,fluid=?,sex=?,temperature=?,pain=?,pill=?,mood=? WHERE date=?",(spotting,fluid,sex,temperature,pain,pill,mood,date))
    conn.commit()
    conn.close()

#To call the function anytime it gets imported.
connect()


# spotting,fluid,sex,temperature,pain,pill,mood
# insert("23-05-2018","HEAVY","STICKY","PROTECTED",96,"LIGHT","TWO TIMES","PMS")

# update("23-05-2018","LIGHT","NOTSTICKY","UNPROTECTED",90,"LIGHT","ONE TIMES","PMS")

# print(view())