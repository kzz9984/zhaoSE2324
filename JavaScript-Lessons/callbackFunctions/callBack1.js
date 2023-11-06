// NOTE: This file contains more comments than usual for learning purposes
// NOTE: Use semicolons; they are the standard style

// Define a higher order function (HoF)
function getUserName(callback) {
    const userName = prompt("Enter your name: ");
    callback(userName);
}

// Callback Function
function greeting(name) {
    document.getElementById('demo').innerHTML = `<h1>Hello ${name}</h1>`;
}

// 1. HoF is called first with a callback function as an arg.
// 2. Once the HoF is called, it will call the callback after it completes its execution
getUserName(greeting);