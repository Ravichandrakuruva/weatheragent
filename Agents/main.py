from fastapi import FastAPI, HTTPException
import os
import requests

app = FastAPI()

# Get API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise Exception("Please set the OPENWEATHER_API_KEY environment variable")

@app.get("/")
def root():
    return {"message": "Weather Agent is running!"}

@app.get("/weather")
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()
