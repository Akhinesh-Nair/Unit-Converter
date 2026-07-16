"""
app.py

Main Flask application for the Universal Unit Converter.
This file handles routing and communicates with converter.py.
"""

from flask import Flask, render_template, request
from converter import convert

# Create Flask application
app = Flask(__name__)


# Home page
@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    category = "Length"
    from_unit = "Meter"
    to_unit = "Kilometer"
    value = ""
    result = None

    #Handle form submission
    if request.method == "POST":

        category = request.form["category"]
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        value = request.form["value"]
        
        try:
            value = float(request.form["value"])

            result = convert(
                category,
                from_unit,
                to_unit,
                value
            )

            converted_value = convert(category, from_unit, to_unit, value)
            result = f"{value} {from_unit} = {converted_value} {to_unit}"

        except ValueError:
            result = "Please enter a valid number."

    return render_template("index.html", 
                           result=result,
                           category=category,
                           from_unit=from_unit,
                           to_unit=to_unit,
                           value=value)


# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)