def WRITE_SCORE(x,s):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="HG@18102003",database="PYTHON")
    mycursor=mydb.cursor()
    sqlform="INSERT INTO PHIGH(Name,Score) VALUES(%s,%s)"
    info=(x,s)
    mycursor.execute(sqlform,info)
    mydb.commit()

def LEADERBOARD():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="HG@18102003",database="PYTHON")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM PHIGH ORDER BY Score")
    
    for s in mycursor:
        print(s)

def CREATE():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="HG@18102003",database="PYTHON")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("CREATE TABLE PHIGH(Name varchar(20) NOT NULL PRIMARY KEY,Score int(3) NOT NULL )")
        print("leader board created")
        mydb.commit()
    except:
        
        mydb.commit()

def DBinit():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",password="HG@18102003")
    mycursor = mydb.cursor()
    try :
        mycursor.execute("CREATE DATABASE PYTHON ")
        print("database created")
        mydb.commit()
    except:
        
        mydb.commit()



