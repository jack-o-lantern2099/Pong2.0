def WRITE_SCORE(x,s):
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="(Yourusername)",password="(YOURPASSWORD)",database="PYTHON")
    mycursor=mydb.cursor()
    sqlform="INSERT INTO PHIGH(Name,Score) VALUES(%s,%s)"
    info=(x,s)
    mycursor.execute(sqlform,info)
    mydb.commit()

def LEADERBOARD():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="username",password="password",database="PYTHON")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM PHIGH ORDER BY Score")
    leader = mycursor.fetchall()
    for s in leader:
        print(s)

def CREATE():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="username",password="password",database="PYTHON")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("SHOW TABLES")
        records=mycursor.fetchall()
        if 'PHIGH' in records:
            x=1
    except:
        mycursor.execute("CREATE TABLE PHIGH(Name varchar(20) NOT NULL PRIMARY KEY,Score int(3) NOT NULL )")
        print("leader board created")
    mydb.commit()
    


