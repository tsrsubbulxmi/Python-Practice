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



#123 subi cse
#234 sudee cse
#345 suru ece

import mysql.connector
import csv
db=mysql.connector.connect(host='localhost',user='root',password='root',database='comp')
cursor=db.cursor()
db.rollback()
print('Before update')
sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i)
sql='update company set salary=10000 where salary<12000'
cursor.execute(sql)
print('Afer update')
sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i)
	
	
	
#Before update
#(123, 'subi', 'cse', 12000)
#(234, 'sudee', 'cse', 10000)
#(345, 'suru', 'ece', 15000)
#Afer update
#(123, 'subi', 'cse', 12000)
##(234, 'sudee', 'cse', 11000)
#(345, 'suru', 'ece', 15000)


import mysql.connector
import csv
db=mysql.connector.connect(host='localhost',user='root',password='root',database='comp')
cursor=db.cursor()
db.rollback()
print('Before delete')
sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i)
sql='delete from company where deptid=\'cse\' and salary < 12000'
cursor.execute(sql)
print('After deleting')
sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i)
	
	
#Before delete
#(123, 'subi', 'cse', 12000)
#(234, 'sudee', 'cse', 10000)
#(345, 'suru', 'ece', 15000)
#After deleting
#(123, 'subi', 'cse', 12000)
#(345, 'suru', 'ece', 15000)
