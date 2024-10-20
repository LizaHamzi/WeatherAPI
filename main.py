# external_api/main.py
from fastapi import FastAPI
from datetime import datetime
import requests
import uvicorn

app = FastAPI()

# You can use an actual weather API (like OpenWeatherMap) for real weather data.
# For the purpose of this example, we'll simulate a weather response.

CITY = 'Ouadhia'
API_KEY = '133e9074a7827085b3445e655203fc80'  # Replace with your real API key

def get_weather():
    # Example weather API endpoint
    
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(weather_url)
        data = response.json()
        
        # Extract relevant data from the API response
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
        }
    except Exception as e:
        weather = {
            'city': 'Unknown',
            'temperature': 'N/A',
            'description': 'Unable to retrieve weather data'
        }
    
    return weather

@app.get("/info")
async def get_info():
    # Get current date and time
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%S")
    
    # Get weather data
    weather = get_weather()
    
    # Return date, time, and weather data
    return {
        "date": formatted_date,
        "time": formatted_time,
        "weather": weather
    }
if __name__ =='__main__':
     uvicorn.run(app, host='0.0.0.0', port =8020, workers=1)