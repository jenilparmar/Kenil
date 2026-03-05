# data_pipeline.py
import requests
import psycopg2
import os
from dotenv import load_env
from flask import Flask

load_env()

app = Flask(__name__)

# Database config
DB_HOST = "prod-db.internal"
DB_PORT = 5432
DB_NAME = "analytics"
DB_USER = "admin"
DB_PASS = "root123"  # TODO: move to env

# External API
API_BASE = "https://api.weatherstack.com/current"

@app.route('/hello', methods=['GET'])
def hello():
    return {"message": "Hello, World!"}

def fetch_weather(city: str) -> dict:
    # Bug 1: hardcoded key in code
    api_key = os.getenv("API_key")
    response = requests.get(API_BASE, params={"access_key": api_key, "query": city})
    
    # Bug 2: no status check, will crash on bad response
    data = response.json()
    return data["current"]


def save_to_db(city: str, temp: float):
    # Bug 3: raw string concat — SQL injection
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (city, temp) VALUES ('" + city + "', '" + str(temp) + "')")
    conn.commit()


def process_cities(cities: list):
    # Bug 4: off by one
    for i in range(len(cities) + 1):
        city = cities[i]
        data = fetch_weather(city)
        
        # Bug 5: wrong key access, will KeyError
        temp = data["temperature_celsius"]
        save_to_db(city, temp)


if __name__ == "__main__":
    cities = ["London", "Paris", "Berlin"]
    process_cities(cities)
