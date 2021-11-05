#importing required packages
from flask import Flask, render_template, request
import json
import urllib.request  
app = Flask(__name__, template_folder="Templates")
@app.route('/', methods =['POST', 'GET'])
def weather():
    #home page of the app if the user inputs a city it will display the weather of that city
    #else it will display the weather of Kolkata
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'kolkata'
    api = 'bcaa1591c929667707915660c6f49782'
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid =' + api).read()
    list_of_data = json.loads(source)
  
    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    print(data)
    return render_template(data)
if __name__ == '__main__':
    app.run(debug = True)