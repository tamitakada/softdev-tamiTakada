# Duckfish - Gavin McGinley, Julia Nelson, Tami Takada
# SoftDev
# K13 -- Template for Success - We created a template to display a list of occupations and one selected occupation.
# 2021-10-10

from flask import Flask, render_template
import csv
import random


def read_occupations(filename: str) -> dict:
    occupations = {}
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)

        next(reader)

        for index, row in enumerate(reader):
            job_class = row[0]
            percentage = row[1]
            occupations[job_class] = float(percentage)

    total_percentage = occupations["Total"]
    occupations["Other"] = 100 - total_percentage
    del occupations["Total"]

    return occupations


def choose_from_dict(occupations: dict) -> str:
    job_classes = list(occupations.keys())
    percentages = list(occupations.values())

    choice = random.choices(job_classes, weights=percentages)[0]
    return choice

app = Flask(__name__)

@app.route("/occupyflaskst")
def get_occupations_page():
    collection = read_occupations("data/occupations.csv")
    
    return render_template(
        "tablified.html",
        header = "Random Occupation",
        collection = collection,
        randomoc = choose_from_dict(collection)
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
