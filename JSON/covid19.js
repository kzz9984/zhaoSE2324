/* JSON Demonstration Using COVID-19 Data
   Populate HTML by dynamically adding rows
 */

async function getData(){

  // Define variables for data
  const state = [];
  const positive = [];

  const tbodyEl = document.querySelector('tbody');  // Select <tbody> element

  const data = await fetch('covid19.json')  // Fetch data
    .then(data => data.json())              // Convert response
    .then(data => {
      //console.log(data);

      // Push JSON to JS arrays & display in table
      for(let i = 0; i < data.length; i++){
        state.push(data[i].state);
        positive.push(data[i].positive);
        //console.log(state[i], positive[i]);

        // Dynamically add table rows to HTML using string interpolation
        tbodyEl.innerHTML += `
        <tr>
          <td class = "state">${state[i]}</td>
          <td class = "positives">${positive[i]}</td>
        </tr>`;
      }
    })
}

getData();