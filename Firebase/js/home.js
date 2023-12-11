// ----------------- Page Loaded After User Sign-in -------------------------//

// ----------------- Firebase Setup & Initialization ------------------------//

/// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } 
  from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

import { getDatabase, ref, set, update, child, get}
  from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyC5bFAmCljLOQ4x7Bg53cuO39WlDeYbacU",
  authDomain: "kz-fd-rtd-demo.firebaseapp.com",
  databaseURL: "https://kz-fd-rtd-demo-default-rtdb.firebaseio.com",
  projectId: "kz-fd-rtd-demo",
  storageBucket: "kz-fd-rtd-demo.appspot.com",
  messagingSenderId: "816016741339",
  appId: "1:816016741339:web:97b844231d9a55ab850dfe"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const auth = getAuth(); // Firebase authentication

// Return an instance of the database associated with your app
const db = getDatabase(app);


// ---------------------// Get reference values -----------------------------

let userLink = document.getElementById('userLink');   // Username for navbar
let signOutLink = document.getElementById('signOut'); // Sign out link
let welcome = document.getElementById('welcome');     // Welcome header
let currentUser = null; // Initialize currentUser to null

// ----------------------- Get User's Name'Name ------------------------------
function getUsername(){
  // Grab value for the 'keep logged in' switch
  let keepLoggedIn = localStorage.getItem("keepLoggedIn");

  // Grab user information passed from signIn.js
  if(keepLoggedIn == "yes"){
    currentUser = JSON.parse(localStorage.getItem('user'));
  }
  else{
    currentUser = JSON.parse(sessionStorage.getItem('user'));
  }
}

// Sign-out function that will remove user info from local/session storage and
// sign-out from FRD
function SignOutUser(){
  sessionStorage.removeItem('user');  // Clear session storage
  localStorage.removeItem('user');    // Clear local storage of user
  localStorage.removeItem('keepLoggedIn');

  signOutLink(auth).then(() => {
      // Sign-out successful
    }).catch((error) => {
      // Error occurred
    });
  
  window.location = "home.html"
}

// ------------------------Set (insert) data into FRD ------------------------
function setData(userID, year, month, day, temperature){
  // Must use brackets around variable name to use it as a key
  set(ref(db, 'users/' + userID + '/data/' + year + '/' + month), {
    [day]: temperature
  })
  .then(() =>{
    alert("Data stored successfully.");
  })
  .catch((error) =>{
    alert("There was an error. Error: " + error);
  });
}

// -------------------------Update data in database --------------------------


// ----------------------Get a datum from FRD (single data point)---------------


// ---------------------------Get a month's data set --------------------------
// Must be an async function because you need to get all the data from FRD
// before you can process it for a table or graph


// Add a item to the table of data



// -------------------------Delete a day's data from FRD ---------------------



// --------------------------- Home Page Loading -----------------------------
window.onload = function() {

  // ------------------------- Set Welcome Message -------------------------
  getUsername();  // Get current user's first name
  if(currentUser == null){
    userLink.innerText = "Create New Account";
    userLink.classList.replace("nav-link", "btn");
    userLink.classList.add("btn-primary");
    userLink.href = "register.html";

    signOutLink.innerText="Sign In"
    signOutLink.classList.replace("nav-link", "btn");
    signOutLink.classList.add("btn-success");
    signOutLink.href = "signIn.html"
  }

  else{
    userLink.innerText = currentUser.firstname;
    welcome.innerText = "Welcome " + currentUser.firstname;
    userLink.classList.replace("btn", "nav-link");
    userLink.classList.add("btn-primary");
    userLink.href = "#";

    signOutLink.innerText="Sign Out"
    signOutLink.classList.replace("btn", "nav-link");
    signOutLink.classList.add("btn-success");
    document.getElementById('signOut').onclick = function(){
      SignOutUser();
    }
  }  

  // Get, Set, Update, Delete Sharkriver Temp. Data in FRD
  // Set (Insert) data function call
  document.getElementById('set').onclick = function(){
    const year = document.getElementById('year').value;
    const month = document.getElementById('month').value;
    const day = document.getElementById('day').value;
    const temperature = document.getElementById('temperature').value;
    const userID = currentUser.uid;

    setData(userID, year, month, day, temperature);
  }
}

  // Update data function call
  

  // Get a datum function call
  

  // Get a data set function call
  

  // Delete a single day's data function call
