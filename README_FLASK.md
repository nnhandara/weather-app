# Weather Forecast Web App (Flask + HTML)

A modern, responsive web-based weather forecast application with a Flask backend API and beautiful HTML/CSS/JavaScript frontend.

## 🌟 Features

- **Current Weather Display** - Real-time weather with beautiful UI
- **5-Day Forecast** - Detailed hourly predictions
- **Interactive Dashboard** - Charts showing temperature, humidity, and wind speed trends
- **Weather Icons** - Visual weather representations
- **Favorite Cities** - Save locations in browser (localStorage)
- **Temperature Units** - Toggle between °C and °F
- **Responsive Design** - Works on desktop, tablet, and mobile
- **RESTful API** - Clean API endpoints for all weather data

## 📁 Project Structure

```
weather-app/
├── app.py                    # Flask backend server
├── static/
│   └── index.html           # Frontend web interface
├── requirements_flask.txt    # Python dependencies
└── README_FLASK.md          # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements_flask.txt
```

This installs:
- Flask (web framework)
- flask-cors (CORS support)
- requests (HTTP library)

### 2. Get API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key from the dashboard

### 3. Configure API Key

Open `app.py` and replace on **line 11**:

```python
API_KEY = "your_api_key_here"
```

With your actual API key:

```python
API_KEY = "abc123your_actual_api_key_here"
```

### 4. Run the Server

```bash
python app.py
```

You should see:

```
==================================================
Weather Forecast API Server
==================================================
Server starting on http://localhost:5000

Available endpoints:
  - GET  /                                    (Main Web Interface)
  - GET  /api/health
  - GET  /api/weather/current?city=<city>&units=<metric|imperial>
  - GET  /api/weather/forecast?city=<city>&units=<metric|imperial>
  - GET  /api/weather/dashboard?city=<city>&units=<metric|imperial>

Press CTRL+C to stop the server
==================================================
```

### 5. Open in Browser

Navigate to: **http://localhost:5000**

## 📖 How to Use

### Web Interface

1. **Search for Weather**
   - Type a city name (e.g., "London", "New York", "Tokyo")
   - Click "Search" or press Enter
   - View results in three tabs

2. **Switch Temperature Units**
   - Use the °C / °F radio buttons
   - Weather data refreshes automatically

3. **Save Favorites**
   - Search for a city
   - Click "Add Current City" button
   - Select from dropdown to quickly load favorites

4. **View Different Data**
   - **Tab 1**: Current weather with detailed metrics
   - **Tab 2**: 5-day forecast with hourly breakdown
   - **Tab 3**: Interactive charts showing weather trends

### API Endpoints

You can also use the API directly:

#### Health Check
```bash
curl http://localhost:5000/api/health
```

#### Current Weather
```bash
curl "http://localhost:5000/api/weather/current?city=London&units=metric"
```

#### 5-Day Forecast
```bash
curl "http://localhost:5000/api/weather/forecast?city=Paris&units=metric"
```

#### Dashboard Data
```bash
curl "http://localhost:5000/api/weather/dashboard?city=Tokyo&units=imperial"
```

## 🎨 Features Breakdown

### Frontend (HTML/CSS/JavaScript)

- **Responsive Design**: Works on all screen sizes
- **Modern UI**: Beautiful gradient background and card-based layout
- **Interactive Charts**: Powered by Chart.js
- **Local Storage**: Favorites saved in browser
- **Real-time Updates**: Async data fetching with fetch API
- **Error Handling**: User-friendly error messages

### Backend (Flask API)

- **RESTful Design**: Clean, predictable API structure
- **CORS Enabled**: Can be used by external frontends
- **Error Handling**: Comprehensive error messages
- **Data Formatting**: Clean JSON responses
- **Static File Serving**: Serves the HTML frontend

## 🔧 API Response Examples

### Current Weather Response
```json
{
  "city": "London",
  "country": "GB",
  "temperature": 15.5,
  "feels_like": 14.2,
  "humidity": 72,
  "pressure": 1013,
  "wind_speed": 4.5,
  "description": "partly cloudy",
  "icon": "02d",
  "visibility": 10.0,
  "timestamp": "2026-02-05T10:30:00"
}
```

### Forecast Response
```json
{
  "city": "London",
  "country": "GB",
  "forecasts": {
    "2026-02-05": [
      {
        "time": "12:00 PM",
        "timestamp": 1707134400,
        "temperature": 16.2,
        "feels_like": 15.1,
        "humidity": 68,
        "wind_speed": 5.2,
        "description": "clear sky",
        "icon": "01d"
      }
    ]
  }
}
```

## 🛠️ Customization

### Change Port

In `app.py`, line 142:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

Change `port=5000` to your desired port.

### Modify UI Colors

In `static/index.html`, edit the CSS variables:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Change the gradient colors to customize the look.

### Add More API Endpoints

Add new routes in `app.py`:

```python
@app.route('/api/weather/alerts')
def get_weather_alerts():
    # Your code here
    pass
```

## 🐛 Troubleshooting

### "404 Not Found" Error

**Problem**: Accessing `http://localhost:5000/` returns 404

**Solution**: 
- Make sure `static/index.html` exists
- Restart the Flask server
- Check the terminal for any errors

### "Invalid API Key" Error

**Problem**: API returns 401 Unauthorized

**Solution**:
- Verify your API key is correct
- Check if it's activated on OpenWeatherMap
- Wait a few minutes after creating the key

### "City Not Found" Error

**Problem**: Cannot find a city

**Solution**:
- Check spelling of city name
- Try with country code: "London,UK"
- Use major cities for testing

### CORS Errors

**Problem**: Frontend can't connect to API

**Solution**:
- Make sure flask-cors is installed
- CORS is already configured in the code
- Check browser console for specific errors

### Charts Not Showing

**Problem**: Dashboard tab shows no charts

**Solution**:
- Check browser console for JavaScript errors
- Make sure Chart.js CDN is accessible
- Try refreshing the page

## 📊 Browser Compatibility

- ✅ Chrome/Edge (v90+)
- ✅ Firefox (v88+)
- ✅ Safari (v14+)
- ✅ Opera (v76+)

## 🔐 Security Notes

- **API Key**: Keep your API key secure
- **Production**: Use environment variables for API keys
- **HTTPS**: Use HTTPS in production
- **Rate Limiting**: Consider adding rate limiting for production

### Using Environment Variables (Recommended)

Instead of hardcoding the API key, use environment variables:

```python
import os
API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your_api_key_here')
```

Then run:

```bash
export OPENWEATHER_API_KEY="your_actual_key"
python app.py
```

## 📝 Development Tips

### Debug Mode

Debug mode is enabled by default. To disable:

```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

### Testing API with Postman

1. Open Postman
2. Create new GET request
3. Enter: `http://localhost:5000/api/weather/current?city=London&units=metric`
4. Click Send

### Adding Logging

Add logging to track requests:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

## 🚀 Deployment

### Deploy to Heroku

1. Create `Procfile`:
```
web: python app.py
```

2. Create `runtime.txt`:
```
python-3.11.0
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Deploy to AWS/DigitalOcean

1. Install gunicorn: `pip install gunicorn`
2. Run: `gunicorn -b 0.0.0.0:5000 app:app`
3. Set up reverse proxy (nginx)

## 📦 What's Included

- ✅ Flask backend with RESTful API
- ✅ Beautiful responsive frontend
- ✅ Current weather display
- ✅ 5-day forecast with hourly breakdown
- ✅ Interactive dashboard with charts
- ✅ Favorites system using localStorage
- ✅ Temperature unit conversion
- ✅ Error handling
- ✅ Weather icons
- ✅ Mobile responsive design

## 📄 License

Free to use for personal and educational purposes.

## 🙏 Credits

- Weather Data: [OpenWeatherMap](https://openweathermap.org/)
- Charts: [Chart.js](https://www.chartjs.org/)
- Backend: [Flask](https://flask.palletsprojects.com/)

## 💡 Future Enhancements

- [ ] Weather alerts and warnings
- [ ] Geolocation support
- [ ] Multiple location comparison
- [ ] Weather maps integration
- [ ] Historical weather data
- [ ] Push notifications
- [ ] User accounts and authentication
- [ ] Weather widget generator
- [ ] Export weather reports (PDF)
- [ ] Dark/Light theme toggle

---

**Enjoy your Weather Forecast App!** 🌈

For issues or questions, check the troubleshooting section above.
