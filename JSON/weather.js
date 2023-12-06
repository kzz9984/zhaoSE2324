/* JSON Demonstration Using Lincroft Weather Data
    1.  Temperatures in Kelvin
    2.  Humidity in %
    3.  Atmospheric Pressue:  hPa = Pa x 100
    4.  Wind Speed: m/s
    5.  Cloudiness: %
    6.  Rain:  mm       Had to convert key "1h" to "h1" (Can't follow # with letter in JS)
 */

async function getData(){

    // Define arrays to store data
    const temp = [];
    const humidity = [];
    const pressure = [];
    const windSpeed = [];
    const rain = [];
    const weather = [];
    const icon = [];

    const data = await fetch('weather.json')    // Fetch data
        .then(data => data.json())              // Convert response to JSON
        .then(data => {
            //console.log(data);

            // Push the JSON data into the JS arrays
            temp.push(data.main.temp);
            humidity.push(data.main.humidity);
            pressure.push(data.main.pressure);
            windSpeed.push(data.wind.speed);
            rain.push(data.rain.h1);
            weather.push(data.weather[0].description);
            console.log(weather);
            icon.push(data.weather[0].icon);

            // Display JSON in HTML table
            document.getElementById("temp").innerHTML = `${temp[0]} K`;
            document.getElementById("humidity").innerHTML = `${humidity[0]} %`;
            document.getElementById("pressure").innerHTML = `${pressure[0]} hPa`;
            document.getElementById("windSpeed").innerHTML = `${windSpeed[0]} m/s`;
            document.getElementById("rain").innerHTML = `${rain[0]} mm`;
            
            // Set weather icon
            document.getElementById("weather").innerHTML = `<img src="img/${icon[0]}.png" alt="rain" width="75">`;

            console.log(temp, humidity, pressure, windSpeed, rain, weather);
        })
}

getData();