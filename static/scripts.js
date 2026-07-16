/*
=========================================
Universal Unit Converter
script.js
=========================================
*/

// Units for each category

const units = {

    Length: [
        "Meter",
        "Kilometer",
        "Centimeter",
        "Millimeter",
        "Mile",
        "Foot",
        "Inch"
    ],

    Weight: [
        "Gram",
        "Kilogram",
        "Pound",
        "Ounce"
    ],

    Temperature: [
        "Celsius",
        "Fahrenheit",
        "Kelvin"
    ],

    Speed: [
        "m/s",
        "km/h",
        "mph"
    ],

    Time: [
        "Second",
        "Minute",
        "Hour",
        "Day"
    ],

    Area: [
        "Square Meter",
        "Square Kilometer",
        "Hectare",
        "Acre"
    ],

    Volume: [
        "Liter",
        "Milliliter",
        "Cubic Meter",
        "Gallon"
    ]

};


// Get HTML elements

const category = document.getElementById("category");

const fromUnit = document.getElementById("from_unit");

const toUnit = document.getElementById("to_unit");

const form = document.querySelector("form");

const resetButton = document.querySelector("button[type='reset']");


// Function to load units

function loadUnits(selectedFrom = "", selectedTo = "") {

    const selectedCategory = category.value;

    // Clear previous options

    fromUnit.innerHTML = "";

    toUnit.innerHTML = "";

    // Add new options

    units[selectedCategory].forEach(unit => {

        let option1 = document.createElement("option");

        option1.value = unit;

        option1.textContent = unit;

        fromUnit.appendChild(option1);


        let option2 = document.createElement("option");

        option2.value = unit;

        option2.textContent = unit;

        toUnit.appendChild(option2);

    });

    // Select second unit by default

    if (selectedFrom) {

        fromUnit.value = selectedFrom; // Set the selected value if provided
    }
    if (selectedTo) {
        toUnit.value = selectedTo;
    }
    else if (toUnit.options.length > 1){
     toUnit.selectedIndex = 1; // Select the second unit by default if no selectedTo is provided   
    }
}


// Change units whenever category changes

category.addEventListener("change", function() { loadUnits(); });



// Form Validation

form.addEventListener("submit", function(event){

    const value = document.querySelector("input[name='value']").value;

    if(value === ""){

        alert("Please enter a value.");

        event.preventDefault();

        return;
    }

    if(isNaN(value)){

        alert("Please enter a valid number.");

        event.preventDefault();

        return;
    }

    if(fromUnit.value === toUnit.value){

        alert("Please choose different units.");

        event.preventDefault();

        return;
    }

});


// Reset Button

resetButton.addEventListener("click", function(){

    setTimeout(() => {

        loadUnits();

    }, 100);

});


// Swap Button

const swapButton = document.getElementById("swap");

swapButton.addEventListener("click", function () {

    let temp = fromUnit.value;

    fromUnit.value = toUnit.value;

    toUnit.value = temp;

});


// Load Length units when page opens

window.onload = function () {
    const selectedFrom = document.body.dataset.from;
    const selectedTo = document.body.dataset.to;
    loadUnits(selectedFrom, selectedTo);
};