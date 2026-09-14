import config
import pymysql

conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_NAME)
cur = conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
cur.execute("select * from customer")
rows = cur.fetchall()   #fetchone() 반복
print(rows)
conn.commit()
conn.close()
