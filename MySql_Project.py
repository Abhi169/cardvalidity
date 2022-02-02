'''Project For Managing The Organisation Records In Remote Database/Tables From One Program'''

#Import mysql-connector module
import mysql.connector as m

def tcreate():
  
    print("Wait Establishing connection with database!")
    db = m.connect(host="db4free.net",user="abhisek",passwd="root4321",database="project_purpose")  #creating connection
    c = db.cursor() 
    
    if db.is_connected():
        print("Database connected successfully!\n")
    else:
        print("Error in connecting the database!\n")
    
    #Taking Input Of Table Name
    tname = input("\nNOTE: Don't use any whitespace in table name\nEnter the table name: ")
    c.execute("create table if not exists {}(Name varchar(20) NOT NULL,Roll_no int(6) NOT NULL UNIQUE);".format(tname))
    #Alerting The user that rollno and name column already exists
    print("\nNOTE: Roll_no and Name columns are created in newly generated table!")
    print("NOTE: Name & Roll_no are Neccesarily Required(cant't be Null)\n")
    #If user want to add more columns
    print("If you want to add more columns enter 1 or else enter 0")
    ch=int(input("Enter 0/1: "))
    if ch==1:
        columns = int(input("\nEnter how many columns you want to add in table: "))
        while(columns>0):
            columns-=1
            cname = input("Enter the column name: ")
            dtype = input("Enter column's datatype: ")
            size = input("Enter the size: ")
            cn = input("Enter constraint if any: ")
            c.execute("alter table {} add({} {}({}) {});".format(tname,cname,dtype,size,cn))
            print("Column Added Successfully!\n")
    if ch==0:
        print("Table created successfully!\n")
    
    input(">>>PRESS ENTER TO CONTINUE<<<")
    return


def add_record():

    print("Wait Establishing connection with database!")
    db = m.connect(host="db4free.net",user="abhisek",passwd="root4321",database="project_purpose")
    c = db.cursor()
    
    if db.is_connected():
        print("Database connected successfully!\n")
    else:
        print("Error in connecting the Database!\n")
    
    c.execute("show tables;")
    print("\nTables Present in Database are: ")
    s = []
    for data in c:
        for info in data:
            #info = info.decode() uncomment this if showing output as bytearray(b'<tablename>')
            print(info)
            s.append(info)
            
    if len(s)==0:
        print("\nDatabase do not contain any Table!")
        print("Create A Table First\n")
    else:
        tname = input("\nEnter the table name in which you want to add records: ")
        #validating table name
        if tname in s:
            c.execute("desc {};".format(tname))
            a=1
            print("\nThe Columns Present in Table Are: ")
            for data in c:
                data = list(data)
                print("{} Column:".format(a),data[0])
                a+=1
                
            ch = 'y'
            while(ch.lower()=='y'):     #if wants to add multiple records
                    
                count = 3
                print()
                name = input("Enter Name: ")
                roll = input("Roll No. is Unique Can't be duplicate\nEnter Roll No: ")
                c.execute("insert into {}(Name,Roll_no)values('{}',{});".format(tname,name,roll))
                db.commit()
                    
                while(count<a):
                  
                        
                    count+=1
                    cname = input("Always Enter Column Name: ")
                    if cname.isspace():
                        while (cname.isspace()==True):
                            print("***Column name is required!***")
                            cname = input("Always Enter Column Name: ")
                
                    value = input("Enter The Input/Data if any: ")
                        
                    if value.isnumeric:
                        c.execute("update {} set {} = '{}' where Roll_no  = {} ;".format(tname,cname,value,roll))
                        db.commit()
                        
                    elif value.isdigit:
                        c.execute("update {} set {} = {} where Roll_no = {} ;".format(tname,cname,value,roll))
                        db.commit()

                
                    print("Data Added Successfully!\n")
                
                ch = input("\nWant to Enter Data y/n: ")
                    

        else:
            print("Table doesn't exist!\n")
  
    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def update():

    print("Wait Establishing connection with database!")
    db = m.connect(host="db4free.net",user="abhisek",passwd="root4321",database="project_purpose")
    c = db.cursor()

    if db.is_connected():
        print("Database connected successfully!\n")
    else:
        print("Error in connecting the Database!\n")

    c.execute("show tables;")
    s=[]
    print("\nTables Present in Database are: ")
    for data in c:
        for info in data:
            #info = info.decode() uncomment this if showing output as bytearray(b'<tablename>')
            print(info)
            s.append(info)
            
    tname = input("\nEnter the table name in which you want to update the records: ")
    if tname in s:
        a = 1
        l =[]
        c.execute("desc {};".format(tname))
        print("\nThe Columns present in table are:")
        for data in c:
            data = list(data)
            print("{} Column:".format(a),data[0])
            l.append(data[0])
            a+=1
                
        print("\nThe following data is in format of {}".format(l))
        print()
        c.execute("select*from {};".format(tname))
        for data in c:
            data = list(data)
            print(data)
                
        ch = 'y'
        while(ch.lower()=='y'):
                
            roll = input("Enter the Roll_no Whose Record You Want to Update: ")
            cname = input("Enter Column Name: ")
            if cname.isspace():
                print("***Column name is required!***")
                cname = input("Enter Column Name: ")
            value = input("Enter The Data/Value: ")
            if value.isnumeric:
                c.execute("update {} set {} = '{}' where Roll_no = {} ;".format(tname,cname,value,roll))
                db.commit()
            elif value.isdigit:
                c.execute("update {} set {} = {} where Roll_no = {} ;".format(tname,cname,value,roll))
                db.commit()
                
            ch = input("Want to Update More Columns y/n: ")
            
    else:
        print("Table do not exist!\n")

    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def rec_deletion():

    print("Wait Establishing connection with database!")
    db = m.connect(host="db4free.net",user="abhisek",passwd="root4321",database="project_purpose")
    c = db.cursor()
    
    if db.is_connected():
        print("Database Connected Successfully!\n")
    else:
        print("Error in connecting the database!\n")
    x=[]
    print("\nThe Tables Present in Database are:")
    c.execute("show tables;")
    for data in c:
        for info in data:
            #info = info.decode()   uncomment this if showing output as bytearray(b'<tablename>')
            print(info)
            x.append(info)
            
    tname = input("\nEnter Table Name: ")
    if tname in x:
        l=[]
        c.execute("desc {};".format(tname))
        for data in c:
            data = list(data)
            l.append(data[0])
                
        c.execute("select*from {};".format(tname))
        print("\nData Inside Table is: ")
        print("\nData is in format of {} respectively\n".format(l))
        for data in c:
            data  = list(data)
            print(data)
                
        roll = input("\nEnter Roll_no whose record you want to delete: ")
        c.execute("delete from {} where roll_no = {};".format(tname,roll))
        db.commit()
        print("Record deleted successfully!\n")
    else:
        print("Table do not exist!\n")

    input(">>>PRESS ENTER TO CONTINUE<<<")
    return


def del_table():

    print("Wait Establishing connection with database!")
    db = m.connect(host="db4free.net",user="abhisek",passwd="root4321",database="project_purpose")
    c = db.cursor()
    
    if db.is_connected():
        print("Connection with Database established successfully\n")
    else:
        print("Error in establishing the connection with Database\n")
    
    print("\nThe Tables Present in Database are:")
    c.execute("show tables;")
    l=[]
    for data in c:
        for info in data:
            #info = info.decode()    uncomment this if showing output as bytearray(b'<tablename>')
            print(info)
            l.append(info)
            
    ch='y'
    while ch.lower()=='y':
        tname = input("\nEnter Table Name Which will be deleted: ")
        if tname in l:
            c.execute("drop table {};".format(tname))
            print("Table Deleted Successfully!")
            db.commit()
                
            print("\nUpdated Tables Are: \n")
            c.execute("show tables;")
            l.clear()
            for data in c:
                for info in data:
                    #info = info.decode()      uncomment this if showing output as bytearray(b'<tablename>')
                    print(info)
                    l.append(info)
                    
            ch=input("\nWant to Delete other Table y/n: ")

        else:
            print("\nTable do not exist!\n")

    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def check_rec():
    
    print("Wait Establishing connection with database!")
    db = m.connect(host="db4free.net",user="abhisek",passwd="root4321",database="project_purpose")
    c = db.cursor()
    
    if db.is_connected():
        print("Connection Established With Database successfully!\n")
    else:
        print("Error in establishing connection with database!\n")
        
    print("\nThe Tables Present in Database are:")
    c.execute("show tables;")
    s=[]
    for data in c:
        for info in data:
            #info = info.decode()    uncomment this if showing output as bytearray(b'<tablename>')
            print(info)
            s.append(info)
            
    if len(s)==0:
        print("\nDatabase do not contain any table\n")
    else:
        tname = input("\nEnter Table Name Whose Record You Want To see: ")
        if tname in s:
            l=[]
            c.execute("desc {};".format(tname))
            for data in c:
                data = list(data)
                l.append(data[0])
                    
            c.execute("select*from {};".format(tname))
            print("Records available in Table Are:")
            print("Records are in following Order respectively:- \n")
            print(l)
            print()
            for data in c:
                data = list(data)
                print(data)
                
            print()

        else:
            print("\nTable doesn't exist\n")

    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def column():
    print("\n1. To Add Column to existing Table\n2. To Delete Column of existing Table")
    ch=int(input("Enter your choice 1/2: "))
    while((ch!=1)and(ch!=2)):
        ch=int(input("Enter valid choice 1/2: "))

    if ch==1:
        
        print("Wait Establishing connection with database!")
        db = m.connect(host="db4free.net",user="abhisek",passwd="root4321",database="project_purpose")
        c = db.cursor()
        
        if db.is_connected():
            print("Connection Established with Database!\n")
        else:
            print("Error in communicating with database!\n")
        c.execute("Show tables;")
        j=[]
        print("\nAvailable Tables are: ")
        for data in c:
            for info in data:
                #info = info.decode()   uncomment this if showing output as bytearray(b'<tablename>')
                print(info)
                j.append(info)

        tname = input("\nEnter Table Name: ")
        if tname in j:
            a=1
            c.execute("desc {};".format(tname))
            print("\nThe availabe columns are: ")
            t=[]
            while a<=len(j):
                for i in c:
                    i = list(i)
                    t.append(i[0])
                    print("{} Column: ".format(a),i[0])
                    a+=1

            cname = input("\nEnter Column Name To Add: ")
            if cname in t:
                print("Column Already Exists!\n")

            else:
                dtype = input("Enter datatype: ")
                size = input("Enter Size: ")
                cn = input("Enter Constraint if any: ")
                c.execute("alter table {} add({} {}({}) {});".format(tname,cname,dtype,size,cn))
                db.commit()
                print("Column created successfully!")
                w = input("Want to See Updated Columns? y/n: ")
                if w.lower()=='y':
                    a=1
                    c.execute("desc {};".format(tname))
                    print("\nUpdated columns are: \n")
                    for data in c:
                        data = list(data)
                        print("{} column: ".format(a),data[0])
                        a+=1

                else:
                    return
        else:
            print("Table do not exist!\n")

    elif ch==2:
        
        print("Wait Establishing connection with database!")
        db = m.connect(host="db4free.net",user="abhisek",passwd="root4321",database="project_purpose")
        c = db.cursor()
        
        if db.is_connected():
            print("Connection Established with Database!\n")
        else:
            print("Error in communicating with database!\n")

        c.execute("Show tables;")
        j=[]
        print("\nAvailable Tables are: ")
        for data in c:
            for info in data:
                #info = info.decode()   uncomment this if showing output as bytearray(b'<tablename>')
                print(info)
                j.append(info)

        tname = input("\nEnter Table Name: ")
        if tname in j:
            a=1
            c.execute("desc {};".format(tname))
            print("The availabe columns are: ")
            t=[]
            while a<=len(j):
                for i in c:
                    i = list(i)
                    t.append(i[0])
                    print("{} Column: ".format(a),i[0])
                    a+=1

            cname = input("\nEnter Column Name To Drop/Delete: ")
            if cname in t:
                c.execute(" alter table {} drop column {};".format(tname,cname))
                db.commit()
                print("Column Deleted Successfully!")
                w = input("Want to See Updated Columns? y/n: ")
                if w.lower()=='y':
                    a=1
                    c.execute("desc {};".format(tname))
                    print("\nUpdated columns are: \n")
                    for data in c:
                        data = list(data)
                        print("{} column: ".format(a),data[0])
                        a+=1

                else:
                    return

            else:
                print("Column do not exist!\n")
        
        else:
            print("Table do not exist!\n")

    print()
    input(">>>ENTER SPACE<<<")
    return

f = True
while f is True:
    print('''
    \n  >>>PROJECT FOR MANAGING THE ORGANISATION RECORDS<<<
          >>>BY USING REMOTE DATABASE<<<     
                           
                     CHOICES                   

    1. To create a new table in database

    2. To add details of student in table

    3. To check the Records present in Table

    4. To delete student's record

    5. To update student's record

    6. To delete a table

    7. To Add/Delete a column

    8. To Exit
    
    ''')
    choice = int(input("Enter Your Choice 1/2/3/4/5/6/7/8: "))

    while((choice!=1)and(choice!=2)and(choice!=3)and(choice!=4)and(choice!=5)and(choice!=6)and(choice!=7)and(choice!=8)):
        choice = int(input("Enter a Valid Choice 1/2/3/4/5/6/7/8: "))


    if choice==1:
        tcreate()

    elif choice==2:
        add_record()

    elif choice==3:
        check_rec()

    elif choice==4:
        rec_deletion()

    elif choice==5:
        update()

    elif choice==6:
        del_table()

    elif choice==7:
        column()


    elif choice==8:
        print("\nTHANK YOU FOR USING THE PROGRAM!\n")
        input("<<<PRESS ENTER>>>")
        f = False
