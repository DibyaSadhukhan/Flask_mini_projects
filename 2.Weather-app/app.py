#importing required packages
from flask import Flask, render_template, request
import json
import requests 
app = Flask(__name__, template_folder="Templates")
@app.route('/', methods =['POST', 'GET'])
def weather():
    #home page of the app if the user inputs a city it will display the weather of that city
    #else it will display the weather of Kolkata
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'kolkata'
    api = "fb33008a8d6dfdee22a79b18a5045d08"
    URL='http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid =' + api
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        return render_template('index.html',temp=temperature,humidity=humidity,pressure=pressure,report=report)
    else:
        return render_template('error.html')
if __name__ == '__main__':
    app.run(debug = True)