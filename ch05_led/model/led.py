import pymysql

class LED:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
        self.cur = self.conn.cursor()
        print("conn ok")

    def get(self):
        self.cur.execute("select * from record_led")
        results = self.cur.fetchall()
        self.conn.commit()
        print(results)
        return results

    def save(self, val: str):
        self.cur.execute(f"insert into record_led(status) values('{val}');")
        self.conn.commit()
        return
