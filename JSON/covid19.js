/* JSON Demonstration Using COVID-19 Data
   Populate HTML by dynamically adding rows
 */

async function getData(){

  // Define variables for data
  const state = [];
  const positive = [];
  const hospitalized = [];

  const tbodyEl = document.querySelector('tbody');  // Select <tbody> element

  const data = await fetch('covid19.json')  // Fetch data
    .then(data => data.json())              // Convert response
    .then(data => {
      //console.log(data);

      // Push JSON to JS arrays & display in table
      for(let i = 0; i < data.length; i++){
        state.push(data[i].state);
        positive.push(data[i].positive);
        hospitalized.push(data[i].hospitalizedCurrently)
        //console.log(state[i], positive[i]);

        // Dynamically add table rows to HTML using string interpolation
        tbodyEl.innerHTML += `
        <tr>
          <td class = "state">${state[i]}</td>
          <td class = "positives">${positive[i]}</td>
        </tr>`;
      }
    })
  
  return {state, positive, hospitalized};
}

async function createChart() {
  const data = await getData();    // createChart will wait until getData() is finished processing
  const ctx = document.getElementById('chart');
  const chart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: data.state,
          datasets: [
            {
                data: data.positive,
                fill: false,
                backgroundColor: 'rgba(0, 0, 0, 1)',
                borderWidth: 0
            }
          ]
      },
      options: {
          responsive: true,   // Re-size based on screen size
          scales: {           // Display options for x & y axes
              x: {
                  title: {
                      display: true,
                      text: 'State',   // x-axis title
                      font: {         // font properties
                          size: 20
                      }
                  },
                  ticks: {
                      autoSkip: false,
                      maxRotation: 90,
                      minRotation: 90,
                      font: {
                          size: 12
                      }
                  }
              },
              y: {
                  title: {
                      display: true,
                      text: 'Positive Cases',
                      font: {
                          size: 20
                      }
                  },
                  ticks: {
                      maxTicksLimit: 20,    // limit # of ticks
                      font: {
                          size: 12
                      }
                  }
              }
          },
          plugins: {          // Display options
              title: {
                  display: true,
                  text: 'Positive COVID-19 Cases vs. State on 6/13/20',
                  font: {
                      size: 24
                  },
                  padding: {
                      top: 10,
                      bottom: 30
                  }
              },
              legend: {
                display: false
              }
          }
      }
  });
}

async function averages() {
    const data = await getData();    // averages will wait until getData() is finished processing
    const positiveEl = document.getElementById('positiveAvg');
    const hospitalizedEl = document.getElementById('hospitalizedAvg');

    // Calculate average of the number of positive cases for all U.S. territories
    let positiveSum = 0;
    for (const state in data.positive) {
        positiveSum += data.positive[state];
    }
    let positiveAvg = positiveSum / data.positive.length;
    positiveEl.textContent += positiveAvg;

    // Calculate average of the number of currently hospitalized cases for all U.S. territories
    let hospitalizedSum = 0;
    for (const state in data.hospitalized) {
        hospitalizedSum += data.hospitalized[state];
    }
    let hospitalizedAvg = hospitalizedSum / data.hospitalized.length;
    hospitalizedEl.textContent += hospitalizedAvg;
}

createChart();
averages();