# 
# SoftDev
# K19 -- A RESTful Journey Skyward

from flask import Flask, render_template
from urllib import request

app = Flask(__name__) 

@app.route("/")       
def home():
    response = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=KG9wjjCgdGoznGvFe5Su5nhnfuCSlt9O10tDLjrl")
    print(response.headers['content'])
    return render_template(
        "main.html"
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
