// Name:    Kevin Zhao
// Date:    12/05/23

// File:    zhao_regex.js

// Purpose: Use regex to validate first name, last name, and email


// Check for null, empty (""), or all spaces only
function isEmptyorSpaces(str) {
    return str === null || str.match(/^ *$/) !== null;
}


// Define variables to test regex code
let firstName = "Kevin";
let lastName = "Zhao";
let email = "kezhao@ctemc.org";


// Validate first name, last name, and email
function validation(firstName, lastName, email) {

    // Define variables with regex code to test user inputs
    let fNameRegex = /^[a-zA-Z]+$/;
    let lNameRegex = /^[a-zA-Z]+$/;
    let emailRegex = /^[a-zA-Z0-9]+@(ctemc|gmail|yahoo)\.(org|com|edu)$/;

    // Return false if any inputs are empty or contain all spaces
    if (isEmptyorSpaces(firstName) || isEmptyorSpaces(lastName) || isEmptyorSpaces(email)) {
        console.log("Please complete all fields.");
        return false;
    }

    // Validate first name
    if (!fNameRegex.test(firstName)) {
        console.log("The first name should only contain letters.");
        return false;
    }

    // Validate last name
    if (!lNameRegex.test(lastName)) {
        console.log("The last name should only contain letters.");
        return false;
    }

    // Validate email
    if (!emailRegex.test(email)) {
        console.log("The email is invalid.");
        return false;
    }

    // Return true if all regex tests are passed
    console.log("All inputs have been validated!");
    return true;
}


// Test regex code
validation(firstName, lastName, email);
