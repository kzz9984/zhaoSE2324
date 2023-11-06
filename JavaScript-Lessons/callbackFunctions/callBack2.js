// NOTE: Daisy chaining callbacks can cause issues; that's where promises come in
//       This is just an example so you know what daisy chaining looks like; it's not the preferred way to code
//       If you see daisy chaining in someone else's code, you should refactor it into promises

// Use callbacks to describe the process to clean your room:
// 1. Clean the room
// 2. Take out the garbage

let cleanRoom = (user, callback) => {
    console.log(user + ' is cleaning the room.');
    callback('Room Cleaned.');
}

let takeGarbageOut = (room, callback) => {
    console.log(room + ' Taking out the garbage');
    callback('Took out the garbage');
}

cleanRoom('Kevin', (roomCleaned) => {               // This callack in an anonymous function
    takeGarbageOut(roomCleaned, (garbageOut) => {  // Output from cleanRoom is a parameter for takeGarbageOut
        console.log(garbageOut);                    // Output from takeGarbageOut
    });
});