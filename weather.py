from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route("/weather/current")
def getWeather():
    try:
        userInput = request.args.get("location", type=str) #Get userinput
        url = "https://api.openweathermap.org/data/2.5/weather?appid=cc438bc00b5f04854e71cdb19490cc45&units=metric&q=" + userInput
        response = requests.get(url)
        json = response.json()
        return [json["name"], json["main"]["temp"], json["main"]["feels_like"]] #Returns location name, temperature and the feels like temperature
    except:
        return "ERROR: Location unavailable, try a different location."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)