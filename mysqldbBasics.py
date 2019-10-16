import pymysql #or import MySQLdb

while True:
    print('''
    Press 1 to create database  Press 2 to create table
    Press 3 to insert           Press 4 update
    Press 5 to to delete        Press 6 to display table
    Press 7 to drop table       Press 8 to drop database
    ''')
    optSel = int(input("Enter your choice and press enter: "))
    if optSel == 1:
        db = pymysql.connect("localhost", "root", "")
        cursor = db.cursor()
        try:
            crtdb = 'create database test'
            cursor.execute(crtdb)
            print("database created")
        except:
            print("database already exists")
    elif optSel == 2:
        try:
            db = pymysql.connect("localhost","root","","test")
            cur = db.cursor()
            try:
                cur.execute('''CREATE TABLE student (
                studentId int primary key,
                name varchar (20) not null,
                age int,
                mark int);''')
                db.commit()
                print("table created")
            except:
                print("Table already exists!!")
        except:
            print("Create database....Press 1")
    elif optSel == 3:
        try:
            db = pymysql.connect("localhost","root","","test")
            cur = db.cursor()
            a = int(input("Enter student id: "))
            b = input("Enter student Name: ")
            c = int(input("Enter age: "))
            d = int(input("Enter the mark: "))
            qry = "insert into student values(%d,'%s',%d,%d);"%(a,b,c,d)
            cur.execute(qry)
            db.commit()
            print("row inserted")
        except:
           print("Create database....Press 1")
    elif optSel == 4:
        try:
            db = pymysql.connect("localhost","root","","test")
            cur = db.cursor()
            a = int(input("Enter student id: "))
            d = int(input("Enter the mark: "))
            qry = "update student set mark=%d where studentId=%d;"%(d,a)
            cur.execute(qry)
            db.commit()
            print("updated row")
        except:
            print("Create database....Press 1")
    elif optSel == 5:
        try:
            db = pymysql.connect("localhost","root","","test")
            cur = db.cursor()
            a = int(input("Enter student id: "))
            qry = "delete from student where studentId=%d;"%(a)
            cur.execute(qry)
            db.commit()
            print("deleted row")
        except:
            print("Create database....Press 1")
    elif optSel == 6:
        try:
            db = pymysql.connect("localhost","root","","test")
            cur = db.cursor()
            qry = "select * from student;"
            cur.execute(qry)
            while True:
                record = cur.fetchone()
                if record == None:
                    break
                print(record)
        except:
            print("Create database....Press 1")

    elif optSel == 7:
        try:
            db = pymysql.connect("localhost","root","","test")
            cur = db.cursor()
            qry = "drop table student;"
            cur.execute(qry)
            db.commit()
            print("table dropped")
        except:
            print("Create database....Press 1")
    elif optSel == 8:
        db = pymysql.connect("localhost","root","")
        cur = db.cursor()
        qry = "drop database test;"
        cur.execute(qry)
        db.commit()
        print("database dropped")
    else:
        print("Enter a valid choice")
