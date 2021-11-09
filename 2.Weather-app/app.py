#importing required packages
from flask import Flask, render_template, request
import json
import requests 
app = Flask(__name__, template_folder="Templates")
@app.route('/', methods =['POST', 'GET'])
def home():
    #home page of the app if the user inputs a city it will display the weather of that city
    #else it will display the weather of Kolkata
    if request.method == 'POST':
        CITY = request.form['city']
    else:
        CITY = "Kolkata"
    API_KEY = "fb33008a8d6dfdee22a79b18a5045d08"
    # upadting the URL
    URL = "https://api.openweathermap.org/data/2.5/weather?q=" + CITY + "&appid=" + API_KEY +"&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        return render_template('index.html',city=CITY,temp=temperature,humidity=humidity,pressure=pressure,report=report)
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug = True)