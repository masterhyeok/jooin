import pymysql

conn = pymysql.connect(host='localhost', user='config.DB_USER', password='q1w2e3', db='shopping_db')
cur = conn.cursor() 
cur.execute("select * from customer")
re = cur.fetchall()
print(re)
cur.close()
conn.close()

