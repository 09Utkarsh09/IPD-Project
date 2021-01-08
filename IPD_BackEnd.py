import sqlite3


def employeeData():
    con=sqlite3.connect("employee.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, emp_id text, Firstname text, Surname text, Dob text, Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()

def addEmpRec(emp_id, Firstname, Surname, Dob, Age, Gender, Address, Mobile):
    con=sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("INSERT INTO employee VALUES (NULL,?,?,?,?,?,?,?,?)",(emp_id , Firstname , Surname , Dob , Age, Gender , Address , Mobile)  )
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employee")
    row = cur.fetchall()
    con.close
    return row

def deleteRec(id):
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("DELETE FROM employee WHERE id=?", (id,))
    con.commit()
    con.close

def searchData(emp_id="", Firstname="", Surname="" , Dob="" , Age="", Gender="" , Address="" , Mobile=""):
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employee WHERE emp_id=? OR Firstname=?   OR Surname=?  OR Dob=?  OR Age=?  OR Gender=?  OR Address=?  OR Mobile=?", (emp_id, Firstname, Surname, Dob, Age, Gender, Address, Mobile))
    row = cur.fetchall()
    con.close()
    return row

def dataUpdate(id,emp_id="", Firstname="", Surname="" , Dob="" , Age="", Gender="" , Address="" , Mobile=""):
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("UPDATE employee SET emp_id=?, Firstname=?, Surname=?, Dob=?, Age=?, Gender=?, Address=?, Mobile=?, WHERE id=?", (emp_id, Firstname,Surname,Dob,Age,Gender,Address,Mobile,id))
    con.commit()
    con.close





employeeData()