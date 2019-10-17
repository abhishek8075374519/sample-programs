import pymysql

adminPass = 'password123#'
balPass = ""

#create database
myDbs1 = pymysql.connect("localhost", "root", "")
cursor = myDbs1.cursor()
try:
    crtdb = 'create database banking;'
    cursor.execute(crtdb)
    print("database created")
except:
    pass

#create table
myDbs1 = pymysql.connect("localhost", "root", "", "banking")
cursor = myDbs1.cursor()
try:
    crtTab = 'create table custDtls(accNo varchar(20) primary key, fName varchar(20), lName varchar(20), eMail varchar(30), mobileN varchar(15), balance int, userName varchar(30) unique, passWord varchar(20));'
    cursor.execute(crtTab)
    print("table created")
except:
    pass

while True:
    currentBalance = 0
    print('''
        Press 1 to add a customer   Press 2 to remove a customer
        Press 3 to view balance     Press 4 to withdraw
        Press 5 to deposit          Press 6 to display table
        ''')
    choice = int(input("enter a choice"))
    if choice==1:
        checkPass = input("Enter admin password:")
        if checkPass==adminPass:
            print("enter customer details")
            accNo = input("enter unique account number: ")
            fName = input("enter first name: ")
            lName = input("eneter last name: ")
            eMail = input("enter Email: ")
            mobileN = input("enter mobile number: ")
            balance = int(input("enter the balance: "))
            userName = input("enter unique username: ")
            passWord = input("enter password: ")
            insCust = "insert into custDtls values('%s', '%s', '%s', '%s', '%s', %d, '%s', '%s');"%(accNo, fName, lName, eMail, mobileN, balance, userName, passWord)
            cursor.execute(insCust)
            myDbs1.commit()
            print("customer added")
        else:
            print("password incorrect")
    elif choice==2:
        checkPass = input("Enter admin password:")
        if checkPass == adminPass:
            accNo = input("enter unique account number: ")
            try:
                remvCust = "delete from custDtls where accNo='%s';"%(accNo)
                cursor.execute(remvCust)
                myDbs1.commit()
                print("customer removed")
            except:
                print("Enter valid accout number")
        else:
            print("password incorrect")
    elif choice==3:
        userName = input("enter username: ")
        passWord = input("enter password: ")
        qry = "select passWord from custDtls where userName='%s';" % (userName)
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record == None:
                break
            balPass = record[0]
            print(balPass)
        if passWord==balPass:
            qry = "select balance from custDtls where userName='%s';"%(userName)
            cursor.execute(qry)
            while True:
                record = cursor.fetchone()
                if record == None:
                    break
                print("Current balance: ",record[0])
        else:
            print("username or password incorrect")
    elif choice==4:
        userName = input("enter username: ")
        passWord = input("enter password: ")
        withAmnt = int(input("enter the amount to be withdrawed"))
        qry = "select passWord from custDtls where userName='%s';" % (userName)
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record == None:
                break
            balPass = record[0]
            print(balPass)
        if passWord == balPass:
            qry = "select balance from custDtls where userName='%s';" % (userName)
            cursor.execute(qry)
            while True:
                record = cursor.fetchone()
                if record == None:
                    break
                currentBalance = (record[0] - withAmnt)
            qry = "update custDtls set balance=%d where userName='%s';"%(currentBalance, userName)
            cursor.execute(qry)
            myDbs1.commit()
            print("Current balance: ", currentBalance)
        else:
            print("username or password incorrect")
    elif choice==5:
        userName = input("enter username: ")
        passWord = input("enter password: ")
        depAmnt = int(input("enter the amount to be deposited"))
        qry = "select passWord from custDtls where userName='%s';" % (userName)
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record == None:
                break
            balPass = record[0]
            print(balPass)
        if passWord == balPass:
            qry = "select balance from custDtls where userName='%s';" % (userName)
            cursor.execute(qry)
            while True:
                record = cursor.fetchone()
                if record == None:
                    break
                currentBalance = (record[0] + depAmnt)
            qry = "update custDtls set balance=%d where userName='%s';" % (currentBalance, userName)
            cursor.execute(qry)
            myDbs1.commit()
            print("Current balance: ", currentBalance)
        else:
            print("username or password incorrect")
    elif choice==6:
        checkPass = input("Enter admin password:")
        if checkPass == adminPass:
            qry = "select * from custDtls;"
            cursor.execute(qry)
            while True:
                record = cursor.fetchone()
                if record == None:
                    break
                print("Account No: ", record[0], " Customer Name: ", record[1], " ", record[2], " Email: ", record[3], " Mobile No: ", record[4], " Current balance: ", record[5], " Username: ", record[6])
        else:
            print("password incorrect")
    else:
        print("enter a valid choice")