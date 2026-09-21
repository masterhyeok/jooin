import pymysql

class TodoDB:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", port=3306, user="root", password="q1w2e3", db="study")
        self.cur = self.conn.cursor()

        print("db conn")

    def get(self):
        self.cur.execute("select * from todos")

        return self.cur.fetchall()

    def add(self, task: str):
        self.cur.execute("insert into todos(task) values('{0}')".format(task))
        self.conn.commit()

    def remove(self, todo_index: int):
        self.cur.execute("delete from todos where todo_index = {}".format(todo_index))
        self.conn.commit()
