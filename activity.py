from flask import Flask
import requests

app = Flask(__name__)

@app.route("/activity/recreational")
def getRecreational():
    try:
        response = requests.get("https://www.boredapi.com/api/activity?type=recreational")
        return response.json()["activity"]
    except:
        return "ERROR while fetching activity: Try again."

@app.route("/activity/relaxation")
def getRelaxation():
    try:
        response = requests.get("https://www.boredapi.com/api/activity?type=relaxation")
        return response.json()["activity"]
    except:
        return "ERROR while fetching activity: Try again."
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)