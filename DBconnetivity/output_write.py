import mysql.connector
import csv
import json
db=mysql.connector.connect(host='localhost',user='root',password='root',database='comp')
cursor=db.cursor()
sql='select * from company'
cursor.execute(sql)			
r=cursor.fetchall()				#fetching all the records
for i in r:
    dic={}
    print(i)
    dic={'id':i[0],'name':i[1],'deptid':i[2],'salary':i[3]}			#creating dictionary 
    c_dic = json.dumps(dic)
    n=str(i[0])+'.json'
    f=open(n,'w')
    f.write(c_dic)
    f.close()
	f=open(n.r)
	print(f.read())
	f.close()
db.commit()
db.close()
