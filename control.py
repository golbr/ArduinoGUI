import serial
from flask import Flask, render_template, request

app=Flask(__name__)

ser=serial.Serial('COM4', 9600, timeout=1)

@app.route("/")
def data():
    while True:
        data = ser.readline()
        if data:
            reading = data.decode('utf-8')
            return render_template('home.html', title='Arduino', reading=reading)

@app.route("/", methods=['POST', 'GET'])
def led():
    if request.method=='POST':
        if request.form['submit']=='LED On ':
            ser.write(str.encode('1'))
        elif request.form['submit']=='LED Off':
            ser.write(str.encode('0'))
    return render_template('home.html', title='Arduino')

if __name__ == "__main__":
    app.run()
