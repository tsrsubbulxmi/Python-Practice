import mysql.connector
import csv
db=mysql.connector.connect(host='localhost',user='root',password='root',database='comp')
cursor=db.cursor()
print('Before delete')
sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i)
sql='delete from company where deptid=\'cse\' and salary < 12000'		#deleting the records whose dept is cse and salary less than 12000
cursor.execute(sql)
print('After deleting')
sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i)
db.commit()
db.close()