// Define Promise
// Promise take 1 function parameter, which has 2 methods: resolve and reject
let promiseToCleanRoom = new Promise((resolve, reject)=>{

    // Part 1: What promise must do (done asynchronously)
    // Clean room

    let isClean = true;     // Is the room clean?

    // Part 2: Execute the promise by resolving or rejecting it
    if (isClean) {
        resolve('clean');       // Passed to .then()
    }
    else {
        reject('not clean');    // Passed to .catch()
    }
});

// Part 3: Call .then() or .catch() when the promise is settled
promiseToCleanRoom.then(fromResolve=>{
    console.log(`The room is ${fromResolve}.`);
}).catch((fromReject) => {
    console.log(`The room is ${fromReject}`);
});