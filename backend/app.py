#!/bin/env python3
from flask import Flask, request
from secrets import Secrets

import calCalc

app = Flask(__name__)
app.config.from_object(Secrets)

@app.route("/createDiet", methods=["POST"])
def home():
    form = request.form
    nutrition_dict = calCalc.person(
        form["gender"].lower(), 'maintain', int(form["weight"]),
        int(form["heightFeet"]), int(form["heightInches"]), int(form["age"]),
        form["activityLevel"].lower())
    return str(nutrition_dict)

if __name__ == "__main__":
    app.run()
