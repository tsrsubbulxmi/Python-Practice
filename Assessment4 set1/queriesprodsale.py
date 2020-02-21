from datetime import datetime

import mysql.connector
import logging
db = mysql.connector.connect(host='localhost', user='root', password='root', database='py_as4')
cursor = db.cursor()

logging.basicConfig(filename="dbcon3.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info(str(datetime.now())+" Database connection established successfully")

class MyError(Exception):
    def __init__(self,str):
        self.value = str


class Queries:
    def q1(self):
        cursor.execute('select product_name,product_code,price from(select product_name,product_code,price,sum(product_quantity),rank()over (order by sum(product_quantity)desc)r from product p join sale s on p.id=s.product_id group by product_id)as ra where r=1')
        r = cursor.fetchall()
        l = ['product_name', 'product_code', 'price']
        print(l[0], l[1], l[2])
        for i in r:
            print(i[0], i[1], i[2])
            logger.info(str(datetime.now())  + " maximum - sold product with product details")

    def q2(self):
        cursor.execute('select product_name,product_code,price from(select product_name,product_code,price,sum(product_quantity),rank()over (order by sum(product_quantity))r from product p join sale s on p.id=s.product_id group by product_id)as ra where r=1')
        r = cursor.fetchall()
        l = ['product_name', 'product_code', 'price']
        print(l[0], l[1], l[2])
        for i in r:
            print(i[0], i[1], i[2])
        logger.info(str(datetime.now()) + " minimum - sold product with product details")

    def q3(self, date1):
        cursor.execute('select product_name,product_code,sum(price) as amount from product p join sale s on s.product_id=p.id group by bill_date having bill_date=%s',
            (date1,))
        r = cursor.fetchall()
        l = ['product_name', 'product_code', 'amount']
        print(l[0], l[1], l[2])
        for i in r:
            print(i[0], i[1], i[2])
        logger.info(str(datetime.now()) + " total amount of products")

    def q4(self, code):
        cursor.execute('select product_name,product_code,price from product where product_code =%s', (code,))
        r = cursor.fetchall()
        l = ['product_name', 'product_code', 'price']
        print(l[0], l[1], l[2])
        for i in r:
            print(i[0], i[1], i[2])
        logger.info(str(datetime.now()) +  " The product fetched with the code")


    def q5(self, id, name, code, price):
        cursor.execute('insert into product values (%s,%s,%s,%s)', (id, 'LG LED TV', 'LED Smart Tv 32LM', 15000))
        cursor.execute('select * from product')
        r = cursor.fetchall()
        l = ['product_id', 'product_name', 'product_code', 'price']
        print(l[0], l[1], l[2], l[3])
        for i in r:
            print(i[0], i[1], i[2], i[3])
        logger.info(str(datetime.now())  + " inserted a record")


q = Queries()
q.q1()
q.q2()
date1 = input('Enter the billing date')
q.q3(date1)
code = input('Enter the product code')
q.q4(code)
print('Enter the id,name,code,price')
id1 = int(input())
name = input()
code = input()
price = int(input())
try:
    if price>50000:
        raise MyError('The price should not exceed 50000')
    else:
        q.q5(id1, name, code, price)
except MyError as e:
    print(e)

db.commit()
db.close()
