from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Weather API URL and key
API_KEY = "3275673718e346e8b0240153240211"
BASE_URL = "http://api.weatherapi.com/v1/current.json"  # Add '/current.json' here

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        
        # Fetch weather data
        response = requests.get(f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no")
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error_message = "City not found or invalid API key."

    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
