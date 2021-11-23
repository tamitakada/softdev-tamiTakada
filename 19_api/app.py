# Tami Takada and Tomas Acuna
# SoftDev
# K19 -- A RESTful Journey Skyward/Making API calls/We got an API key from NASA Open APIs and displayed an image from NASA using the key.
# 2021-11-23

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__) 

@app.route("/")       
def home():
    key = ""
    with open("key_nasa.txt") as f:
        lines = f.readlines()
        key = lines[0]
#        print(key)

    response = request.urlopen(f"https://api.nasa.gov/planetary/apod?api_key={key}")
    dict = json.loads(response.read())
#    print(dict)

    return render_template(
        "main.html",
        pic = dict["url"],
        explanation = dict["explanation"]
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
