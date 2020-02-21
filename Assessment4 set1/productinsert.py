import mysql.connector
import csv
import datetime
from datetime import datetime
import logging
db = mysql.connector.connect(host='localhost', user='root', password='root', database='py_as4')
cursor = db.cursor()
logging.basicConfig(filename="dbcon1.log",format='%(asctime)s %(message)s',filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info(str(datetime.now())+" Database connection established successfully")
f=open('product.csv','r')
l=csv.reader(f)
k=1
for i in l:
    cursor.execute('insert into product values (%s,%s,%s,%s)',i)
    logger.info(str(datetime.now())+"row "+str(k)+" inserted successfully")
    k=k+1
cursor.execute('select * from product')
r=cursor.fetchall()
for i in r:
    print(i)
db.commit()
db.close()