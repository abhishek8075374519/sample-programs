import sqlite3
import os

while True:
    print('''
    Press 1 to create table     Press 2 to insert
    Press 3 to update           Press 4 to delete
    Press 5 to display table    Press 6 to drop table
    Press 7 to drop database
    ''')
    optSel = int(input("Enter your choice and press enter: "))
    if optSel == 1:
        db = sqlite3.connect('data.db')
        cur = db.cursor()
        try:
            cur.execute('''CREATE TABLE student (
            studentId int primary key,
            name varchar (20) not null,
            age int,
            mark int);''')
            db.commit()
        except:
            print("Table already exists!!")
    elif optSel == 2:
        db = sqlite3.connect('data.db')
        cur = db.cursor()
        a = int(input("Enter student id: "))
        b = input("Enter student Name: ")
        c = int(input("Enter age: "))
        d = int(input("Enter the mark: "))
        qry = "insert into student values(?,?,?,?);"
        cur.execute(qry,(a,b,c,d))
        db.commit()
    elif optSel == 3:
        db = sqlite3.connect('data.db')
        cur = db.cursor()
        a = int(input("Enter student id: "))
        d = int(input("Enter the mark: "))
        qry = "update student set mark=%d where studentId=%d;"%(d,a)
        cur.execute(qry)
        db.commit()
    elif optSel == 4:
        db = sqlite3.connect('data.db')
        cur = db.cursor()
        a = int(input("Enter student id: "))
        qry = "delete from student where studentId=%d;"%(a)
        cur.execute(qry)
        db.commit()
    elif optSel == 5:
        db = sqlite3.connect('data.db')
        cur = db.cursor()
        qry = "select * from student;"

        cur.execute(qry)
        while True:
            record = cur.fetchone()
            if record == None:
                break
            print(record)

    elif optSel == 6:
        db = sqlite3.connect('data.db')
        cur = db.cursor()
        qry = "drop table student;"
        cur.execute(qry)
        db.commit()
    elif optSel == 7:
        os.remove('data.db')
        print("Database dropped")
    else:
        print("Enter a valid choice")
