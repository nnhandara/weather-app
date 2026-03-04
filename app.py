import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests
from datetime import datetime

from collections import defaultdict

app = Flask(__name__, static_folder='static')
CORS(app)

# OpenWeatherMap API Configuration
API_KEY = "69b9d510de193690c30b59bc5f8e58f3"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
ICON_URL = "http://openweathermap.org/img/wn/{}@2x.png" 

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(app.static_folder, 'images'), filename)

@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_from_directory('static', 'index.html')

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/weather/current')
def get_current_weather():
    """Get current weather for a city"""
    city = request.args.get('city')
    units = request.args.get('units', 'metric')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    if API_KEY == "your_api_key_here":
        return jsonify({'error': 'Please set your OpenWeatherMap API key'}), 500
    
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': units
        }
        
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Format the response
        result = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'visibility': data.get('visibility', 0) / 1000,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(result)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return jsonify({'error': f'City "{city}" not found'}), 404
        elif response.status_code == 401:
            return jsonify({'error': 'Invalid API key'}), 401
        else:
            return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/weather/forecast')
def get_forecast():
    """Get 5-day forecast for a city"""
    city = request.args.get('city')
    units = request.args.get('units', 'metric')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    if API_KEY == "your_api_key_here":
        return jsonify({'error': 'Please set your OpenWeatherMap API key'}), 500
    
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': units
        }
        
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
                # Group forecast by date
        grouped_forecasts = defaultdict(list)

        for item in data['list']:
            dt = datetime.fromtimestamp(item['dt'])
            date_key = dt.strftime('%Y-%m-%d')

            grouped_forecasts[date_key].append({
                'time': dt.strftime('%H:%M'),
                'temperature': item['main']['temp'],
                'description': item['weather'][0]['description'],
                'icon': item['weather'][0]['icon'],
                'humidity': item['main']['humidity'],
                'wind_speed': item['wind']['speed']
            })

        result = {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'forecasts': dict(grouped_forecasts),  # ✅ EXACT key frontend needs
            'units': units
        }

        return jsonify(result)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return jsonify({'error': f'City "{city}" not found'}), 404
        else:
            return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/weather/dashboard')
def get_dashboard_data():
    """Get weather data for dashboard charts"""
    city = request.args.get('city')
    units = request.args.get('units', 'metric')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    if API_KEY == "your_api_key_here":
        return jsonify({'error': 'Please set your OpenWeatherMap API key'}), 500
    
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': units
        }
        
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract data for charts
        timestamps = []
        temperatures = []
        humidity_values = []
        wind_speeds = []
        
        for item in data['list']:
            timestamps.append(datetime.fromtimestamp(item['dt']).isoformat())
            temperatures.append(item['main']['temp'])
            humidity_values.append(item['main']['humidity'])
            wind_speeds.append(item['wind']['speed'])
        
        result = {
            'city': data['city']['name'],
            'timestamps': timestamps,
            'temperatures': temperatures,
            'humidity': humidity_values,
            'wind_speeds': wind_speeds,
            'unit': units
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("Weather Forecast API Server")
    print("="*50)
    print("Server starting on http://localhost:5090")
    print("\nAvailable endpoints:")
    print("  - GET  /                                                    (Main Web Interface)")
    print("  - GET  /api/health")
    print("  - GET  /api/weather/current?city=<city>&units=<metric|imperial>")
    print("  - GET  /api/weather/forecast?city=<city>&units=<metric|imperial>")
    print("  - GET  /api/weather/dashboard?city=<city>&units=<metric|imperial>")
    print("\nPress CTRL+C to stop the server")
    print("="*50 + "\n")


    port = int(os.environ.get("PORT", 5090))
    app.run(debug=True,use_reloader=True,host="0.0.0.0", port=port)