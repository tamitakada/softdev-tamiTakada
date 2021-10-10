# Duckfish - Gavin McGinley, Julia Nelson, Tami Takada
# SoftDev
# K13 -- Template for Success - We created a template to display a list of occupations and one selected occupation.
# 2021-10-10

from flask import Flask, render_template
import occupations

app = Flask(__name__)

@app.route("/occupyflaskst")
def get_occupations_page():
    collection = occupations.read_occupations("occupations.csv")
    
    return render_template(
        'occupyflaskst.html',
        collection = collection,
        randomoc = occupations.choose_from_dict(collection)
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
