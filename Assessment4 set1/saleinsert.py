import mysql.connector
import csv
from datetime import datetime
import logging
db = mysql.connector.connect(host='localhost', user='root', password='root', database='py_as4')
cursor = db.cursor()

logging.basicConfig(filename="dbcon2.log",format='%(asctime)s %(message)s',filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info(str(datetime.now())+" Database connection established successfully")
k=1
f=open('sale.csv','r')
l=csv.reader(f)
for i in l:
    cursor.execute('insert into sale values (%s,%s,%s,%s)',i)
logger.info(str(datetime.now()) +" data insertion in sale table is success")
cursor.execute('select * from sale')
r=cursor.fetchall()
for i in r:
    print(i)
db.commit()
db.close()