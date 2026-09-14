from flask import Flask

app = Flask(__name__)
@app.route('/hello')
def hello():
    return "hello" + " " + "world"

@app.route('/hi')
def hi():
    return "hi world"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5001)
