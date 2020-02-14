import mysql.connector
import csv
db=mysql.connector.connect(host='localhost',user='root',password='root',database='comp')
cursor=db.cursor()
f=open('data.csv','r')
l=csv.reader(f)
for i in l:
    cursor.execute('insert into company(id,name,deptid,salary) values(%s,%s,%s,%s)',i)

sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i[0],i[1],i[2])
db.commit()
db.close()