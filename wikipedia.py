from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route("/wikipedia/information")
def getInformation():
    try:
        userInput = request.args.get("input", type=str)
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + userInput
        response = requests.get(url)
        return response.json()["extract"]
    except:
        return "ERROR: Try a different search term."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)