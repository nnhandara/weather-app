# Weather Forecast API - Backend

Flask-based REST API backend for the Weather Forecast application.

## Features

- RESTful API endpoints for weather data
- Current weather information
- 5-day weather forecast
- Dashboard time series data
- Comprehensive error handling
- CORS enabled for frontend communication

## API Endpoints

### 1. Health Check
```
GET /api/health
```
Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "message": "Weather API Backend is running"
}
```

### 2. Current Weather
```
GET /api/weather/current?city=<city_name>&units=<metric|imperial>
```

**Parameters:**
- `city` (required): City name (e.g., "London", "New York")
- `units` (optional): Temperature units - "metric" (°C) or "imperial" (°F). Default: "metric"

**Example:**
```
GET /api/weather/current?city=London&units=metric
```

**Response:**
```json
{
  "city": "London",
  "country": "GB",
  "temperature": 15.5,
  "feels_like": 14.2,
  "humidity": 72,
  "pressure": 1013,
  "wind_speed": 5.5,
  "description": "partly cloudy",
  "icon": "02d",
  "icon_url": "http://openweathermap.org/img/wn/02d@2x.png",
  "units": "metric"
}
```

### 3. 5-Day Forecast
```
GET /api/weather/forecast?city=<city_name>&units=<metric|imperial>
```

**Parameters:**
- `city` (required): City name
- `units` (optional): Temperature units. Default: "metric"

**Example:**
```
GET /api/weather/forecast?city=Tokyo&units=metric
```

**Response:**
```json
{
  "city": "Tokyo",
  "country": "JP",
  "forecast": [
    {
      "timestamp": 1638360000,
      "datetime": "2024-12-01T12:00:00",
      "temperature": 18.5,
      "humidity": 65,
      "wind_speed": 3.5,
      "description": "clear sky",
      "icon": "01d",
      "pop": 0.1
    }
    // ... more forecast items
  ],
  "units": "metric"
}
```

### 4. Dashboard Data
```
GET /api/weather/dashboard?city=<city_name>&units=<metric|imperial>
```

Returns time series data formatted for dashboard visualization.

**Example:**
```
GET /api/weather/dashboard?city=Paris&units=metric
```

**Response:**
```json
{
  "city": "Paris",
  "country": "FR",
  "timestamps": ["2024-12-01T12:00:00", "2024-12-01T15:00:00", ...],
  "temperatures": [15.5, 16.2, 17.1, ...],
  "humidity": [72, 68, 65, ...],
  "wind_speeds": [5.5, 6.2, 5.8, ...],
  "units": "metric"
}
```

## Setup Instructions

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure API Key

Open `app.py` and replace the API key on line 11:

```python
API_KEY = "your_api_key_here"
```

Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

### 3. Run the Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- `400 Bad Request`: Missing required parameters
- `401 Unauthorized`: Invalid API key
- `404 Not Found`: City not found or invalid endpoint
- `500 Internal Server Error`: Server-side error
- `503 Service Unavailable`: Connection error
- `504 Gateway Timeout`: Request timeout

**Error Response Format:**
```json
{
  "error": "Error message description"
}
```

## Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:5000/api/health

# Get current weather
curl "http://localhost:5000/api/weather/current?city=London&units=metric"

# Get forecast
curl "http://localhost:5000/api/weather/forecast?city=Tokyo&units=imperial"

# Get dashboard data
curl "http://localhost:5000/api/weather/dashboard?city=Paris&units=metric"
```

### Using Postman or Browser

Simply navigate to:
```
http://localhost:5000/api/weather/current?city=London&units=metric
```

## Configuration

### Port Configuration
Change the port in `app.py` (last line):
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your desired port
```

### Debug Mode
For production, set `debug=False`:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## CORS Configuration

CORS is enabled for all origins. To restrict access, modify in `app.py`:

```python
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
```

## Dependencies

- **Flask**: Web framework for API
- **Flask-CORS**: Enable Cross-Origin Resource Sharing
- **requests**: HTTP library for OpenWeatherMap API calls

## Architecture

```
Backend (Flask API)
    ↓
OpenWeatherMap API
    ↓
Weather Data
    ↓
Frontend (Tkinter GUI)
```

## Production Deployment

For production deployment, consider:
1. Using a production WSGI server (Gunicorn, uWSGI)
2. Setting up environment variables for API keys
3. Implementing rate limiting
4. Adding authentication
5. Using HTTPS
6. Setting up proper logging

### Example with Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>
```

### API Key Issues
- Verify your API key is active on OpenWeatherMap
- Check you've replaced "your_api_key_here" in the code
- Wait a few minutes after creating a new API key

### CORS Errors
- Ensure Flask-CORS is installed
- Check that CORS(app) is called after creating the Flask app

## License

Open source - available for personal and educational use.
