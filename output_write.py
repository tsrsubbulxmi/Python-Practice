import mysql.connector
import csv
import json
db=mysql.connector.connect(host='localhost',user='root',password='root',database='comp')
cursor=db.cursor()
