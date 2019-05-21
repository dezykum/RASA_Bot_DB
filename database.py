# import sqlite3
 
# from sqlite3 import Error
 
# def sql_connection():
 
#     try:
 
#         con = sqlite3.connect('mydatabase.db')
 
#         return con
 
#     except Error:
 
#         print(Error)
 
# def sql_table(con):
 
#     cursorObj = con.cursor()
 
#     # cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
#     cursorObj.execute("INSERT INTO employees VALUES(2, 'Andrew', 800, 'HR', 'Manager', '2019-01-08')")
 
#     con.commit()
 
# con = sql_connection()
 
# sql_table(con)
import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_fetch(con):
        cursorObj = con.cursor()
        # data = [(3, "Raj","900","Technical","Developer","2016-04-22"), (4, "Rohan","1000","Technical","Analyst","2018-04-17"), (5, "Roger","900","Technical","Developer","2016-04-22"), (6, "Neha","900","Digital","Tester","2016-04-08")]
        cursorObj.execute('SELECT name, SUM(salary) FROM employees GROUP BY NAME;')
        rows = cursorObj.fetchall()
        print(rows)
        for row in rows:
                print(row)
 
sql_fetch(con)

