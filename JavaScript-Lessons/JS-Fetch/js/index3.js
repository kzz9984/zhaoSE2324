/* Use JS Fetch to get image data and convert it to an image element
using async and await. Async and await can be used to condense
.then() code to make it more readable.

--- Await keyword can only be used with Async functions
--- Async functions by definition return a promise */

const imageUrl="https://images.unsplash.com/photo-1570288685369-f7305163d0e3?q=80&w=2864&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
console.log('Fetching panda image');

async function getImage(){
// Await result of fetch and store it in response
const response = await fetch(imageUrl);
const blob = await response.blob(); // Convert response to blob

// Convert blob to a proper HTML object URL
document.getElementById('panda').src = URL.createObjectURL(blob);
}

getImage()
.then(response => {
console.log('Done')     // Process works
})
.catch(error => {
console.log('Error message: '); // Indicate Error
console.log(error);
});