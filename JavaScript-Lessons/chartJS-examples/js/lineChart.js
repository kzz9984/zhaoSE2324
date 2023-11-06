/*
    Demonstrate how to create a line chart
*/

async function getData() {
    const response = await fetch('../data/global-mean-temp.csv');
    const data = await response.text();     // CSV is in TEXT format
    console.log(data);

    const xYears = [];      // x-axis labels = years values
    const yTemps = [];      // y-axis global temp values
    const yNHtemps = [];    // y-axis NH temp values
    const ySHtemps = [];    // y-axis SH temp values

    // \n - new line character
    // split('\n') will separate table into an array of indiv. rows
    // slice(start, end) - return a new array starting at index start
    //                     up to but not including index end.
    const table = data.split('\n').slice(1);
    console.log(table);

    table.forEach(row => {
        const columns = row.split(',');         // split each row on the commas
        const year = columns[0];                // assign year value
        xYears.push(year);                      // push year value into xYears array

        const temp = parseFloat(columns[1]);    // assign temp values
        yTemps.push(temp + 14);                 // push temp values + 14 to store mean temp values

        const nhTemp = parseFloat(columns[2]);  // n. hemi. temp deviation values
        yNHtemps.push(nhTemp + 14);

        const shTemp = parseFloat(columns[3]);  // s. hemi. temp deviation values
        ySHtemps.push(shTemp + 14);

        console.log(year, temp, nhTemp, shTemp);
    })
}

getData();