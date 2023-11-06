import mysql.connector as mp

conn = mp.connect(host='localhost' , user='root', passwd='Adi9303@',database='school')
cur = conn.cursor()
#cur.execute("Create table nitin(id int,name varchar(20))")
cur.execute("insert into nitin1 values(1,'xyz');")
# cur.execute("insert into nitin1 values(2,'aaa');")
# cur.execute("insert into nitin1 values(3,'bbb');")
# cur.execute("insert into nitin1 values(4,'abc');")
id=int(input("Enter id:"))
name=input("Enter name:")
val = [id,name]
state = "insert into nitin1 values(%s,%s)"
cur.execute(state,val)
cur.execute("select*from nitin1")
 
data = cur.fetchall()
for i in data:
    print(i)
conn.commit()