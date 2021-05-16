import sqlite3

from sqlite3 import Error

def sql_connection(): 
    try: 
        con = sqlite3.connect('mydatabase.db')
        print('БД подключено')
        return con
    except Error:
        print(Error)
    #finally:
        #con.close()

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE emp(id integer PRIMARY KEY, name text, salary real, departament text, position text, hireDate text)")
    con.commit()

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO emp(id, name, salary, departament, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()
def sql_select(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM emp WHERE emp.id = 1')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)


entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

con = sql_connection()
#sql_table(con)
#sql_insert(con,entities)
sql_select(con)
