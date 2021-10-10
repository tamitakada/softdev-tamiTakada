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
