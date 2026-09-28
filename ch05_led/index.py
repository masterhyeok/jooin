from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from model.led import LED

app = Flask(__name__)
led_model = LED()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

def on():
    try:
        GPIO.output(8, GPIO.HIGH)
        led_model.save("on")
        return "ok"
    except:
        print("on error")
        return "no"

def off():
    try:
        GPIO.output(8, GPIO.LOW)
        led_model.save("off")
        return "ok"
    except:
        print("off error")
        return "no"

@app.route("/")
def index():
    led_model.get()
    return render_template("index.html")

@app.route("/led", methods=["PATCH"])
def turn():
    r = request.data
    if (r == b"1"):
        return on()
    elif (r == b"0"):
        return off()
    return "nah"

if __name__ == "__main__":
    led_model.get()
    app.run(host="0.0.0.0", port=5002)
