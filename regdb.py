import mysql.connector
def db(rool_num,dob,file):
    # x =self.textEdit.text()
    # print(x)
    try:

        mydb = mysql.connector.connect(
            host="localhost",
            user="ajith",
            password="main",
            db="python"
        )
        print(mydb)
        mys = mydb.cursor()
        search = "SELECT * FROM student WHERE roolnumber="
        new = str(rool_num)
        new1: str = "'"
        new2: str = "'"
        new3=" and dob ="
        new4=str(dob)
        new6=new1+new4+new2
        new5=new3+new6
        request: str = new1 + new + new2+new5
        qry = search + request
        print(qry)
        mys.execute(qry)
        result = mys.fetchall()
        if result==0:
            print("no user")
        else:
            s1 = "UPDATE student SET img="
           # s2=
            s3=  " WHERE roolnumber= "
            s4=    "and dob="
            s5="'"


            val = ("John", "Highway 21")
           # mys.execute(sql, val)



    except:
        print("error")
        return 0

