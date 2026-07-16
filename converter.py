"""
converter.py

Contains all conversion functions used by the Flask application.
"""


def convert(category, from_unit, to_unit, value):

    # LENGTH
    if category == "Length":

        units = {
            "Meter": 1,
            "Kilometer": 1000,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Foot": 0.3048,
            "Inch": 0.0254
        }

        meters = value * units[from_unit]

        return round(meters / units[to_unit], 4)

    # WEIGHT
    elif category == "Weight":

        units = {
            "Gram": 1,
            "Kilogram": 1000,
            "Pound": 453.592,
            "Ounce": 28.3495
        }

        grams = value * units[from_unit]

        return round(grams / units[to_unit], 4)

    # TEMPERATURE
    elif category == "Temperature":

        if from_unit == to_unit:
            return value

        if from_unit == "Celsius":

            if to_unit == "Fahrenheit":
                return round((value * 9/5) + 32, 2)

            elif to_unit == "Kelvin":
                return round(value + 273.15, 2)

        elif from_unit == "Fahrenheit":

            if to_unit == "Celsius":
                return round((value - 32) * 5/9, 2)

            elif to_unit == "Kelvin":
                return round((value - 32) * 5/9 + 273.15, 2)

        elif from_unit == "Kelvin":

            if to_unit == "Celsius":
                return round(value - 273.15, 2)

            elif to_unit == "Fahrenheit":
                return round((value - 273.15) * 9/5 + 32, 2)

    # SPEED
    elif category == "Speed":

        units = {
            "m/s": 1,
            "km/h": 0.277778,
            "mph": 0.44704
        }

        base = value * units[from_unit]

        return round(base / units[to_unit], 4)

    # TIME
    elif category == "Time":

        units = {
            "Second": 1,
            "Minute": 60,
            "Hour": 3600,
            "Day": 86400
        }

        base = value * units[from_unit]

        return round(base / units[to_unit], 4)

    # AREA
    elif category == "Area":

        units = {
            "Square Meter": 1,
            "Square Kilometer": 1000000,
            "Hectare": 10000,
            "Acre": 4046.86
        }

        base = value * units[from_unit]

        return round(base / units[to_unit], 4)

    # VOLUME
    elif category == "Volume":

        units = {
            "Liter": 1,
            "Milliliter": 0.001,
            "Cubic Meter": 1000,
            "Gallon": 3.78541
        }

        base = value * units[from_unit]

        return round(base / units[to_unit], 4)

    return "Conversion not supported."