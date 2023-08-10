import sqlite3 
from datetime import datetime,timedelta


def connect():
    '''
    A function to create connection with database and create a cursor.
    It also checks whether there is a table present if not it creates a new one.
    '''
    try:
        conn = sqlite3.connect('notes.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS note(date text, spotting text, fluid text, sex text, temperature integer, pain text, pill text, mood text)")
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

def insert(date,spotting,fluid,sex,temperature,pain,pill,mood):
    """
    This function helps to insert the data into the database.
    """
    try:
        conn = sqlite3.connect('notes.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO note VALUES (?,?,?,?,?,?,?,?)",(date,spotting,fluid,sex,temperature,pain,pill,mood))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

def view():
    """
    This function allows to retrieve all the data from the table of the database.
    Returns rows as a tuple 
    """
    try:
        conn = sqlite3.connect('notes.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM note")
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

# TO WORK
def search(date):
    try:
        conn = sqlite3.connect('notes.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM note WHERE date=?", (date,))
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print("An error occurred:", e)
        return None  # Return None to indicate failure
    finally:
        if conn:
            conn.close()

def delete(date):
    try:
        conn = sqlite3.connect('notes.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM note WHERE date=?", (date,))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

def update(date,spotting,fluid,sex,temperature,pain,pill,mood):
    try:
        conn = sqlite3.connect('notes.db')
        cur = conn.cursor()
        cur.execute("UPDATE note SET spotting=?,fluid=?,sex=?,temperature=?,pain=?,pill=?,mood=? WHERE date=?", (spotting,fluid,sex,temperature,pain,pill,mood,date))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

#To call the function anytime it gets imported.
connect()


# spotting,fluid,sex,temperature,pain,pill,mood
# insert("23-05-2018","HEAVY","STICKY","PROTECTED",96,"LIGHT","TWO TIMES","PMS")

# update("23-05-2018","LIGHT","NOTSTICKY","UNPROTECTED",90,"LIGHT","ONE TIMES","PMS")

# print(view())
