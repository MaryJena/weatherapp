from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'your_openweathermap_api_key'  # Replace with your API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if city:
        response = requests.get(BASE_URL, params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        })
        data = response.json()
        if data['cod'] == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
            return render_template('weather.html', weather=weather_data)
        else:
            return render_template('weather.html', error=data['message'])
    return render_template('index.html', error='City is required')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)