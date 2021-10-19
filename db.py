import mysql.connector

def write(image,photo):
    with open(photo,'wb')as file:
        file.write(image)


def db(rool_num,dob):
    # x =self.textEdit.text()
    # print(x)
    try:

        mydb = mysql.connector.connect(host="localhost",user="root",password="",db="ajith")
        print(mydb)
        mys = mydb.cursor()
        print(mys)


        # mysursor.execute("CREATE DATABASE python")
        # mys.execute("CREATE TABLE exam6(rolnum int,name varchar(20));")
        # mys.execute("INSERT INTO exam6 (rolnum, name) VALUES ('2322', 'aasdlkksa');")

        search = "SELECT * FROM sdata WHERE roolnumber="
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
        for row in result:
            #print("Name",row[1])
            image=row[3]
            write(image,"imag1.jpg")
        return result 

    except:
        print("error")
        return 0

