import mysql.connector
import csv
import json
db=mysql.connector.connect(host='localhost',user='root',password='root',database='comp')
cursor=db.cursor()
print('Before update')
sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i)
sql='update company set salary=11000 where salary<12000'		#updating the salary to 11000 when salar <12000
cursor.execute(sql)
print('Afer update')
sql='select * from company'
cursor.execute(sql)
r=cursor.fetchall()
for i in r:
    print(i)
    dic={'id':i[0],'name':i[1],'deptid':i[2],'salary':i[3]}		#after update selecting the records
    c_dic=json.dumps(dic)
    print(c_dic)
db.commit()
db.close()