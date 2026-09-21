from flask import Flask, render_template
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='q1w2e3' db='study')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<num>")
def up(num: int):
    print(num)

    cur = conn.cursor()
    cur.execute("insert into numcount(num) values({0})".format(num))
    conn.commit()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
