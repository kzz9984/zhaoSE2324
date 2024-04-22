'''
Name: Kevin Zhao
File: zhaoWeather.py
Date: 04/15/2024

Purpose: Create a weather app GUI to display the weather data of a city inputted by the user

'''

import tkinter as tk            # GUI module
from tkinter import font        # Change font properties
import requests                 # Access API
import json                     # Format JSON
from PIL import Image, ImageTk  # Image Module

# Test the button
def test_button(entry):         # Test with entry parameter
    print('The city entered was:', entry)

# Request and get weather information using API
def get_weather(city):
    weather_key = '337c419e8cb31c9c3a7c91f110c72d02'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'
    units = 'imperial'

    # Test url for API
    #print(url.format(city, units, weather_key))

    # Save API response (returned as a response object)
    response = requests.get(url.format(city, units, weather_key))

    # Convert the response to a Python dictionary
    weather = response.json()
    #print(weather)

    # Set label text with weather description
    label['text'] = format_response(weather)

    # Set icon in label
    icon_name = weather['weather'][0]['icon']
    print(icon_name)
    open_image(icon_name)

def format_response(weather):
    try:
        name = weather['name']                      # City
        desc = weather['weather'][0]['description'] # This is a list so you have to index it
        temp = weather['main']['temp']              # Temperature
        fl = weather['main']['feels_like']          # "Feels like" temperature
        hum = weather['main']['humidity']           # Humidity
        ws = weather['wind']['speed']               # Wind speed
        ds = u'\N{DEGREE SIGN}' # Degree symbol

        label_text = 'City: {}\nWeather: {}\nTemperature: {}{}F\nFeels Like: {}{}F\nHumidity: {}%\nWind Speed: {} mph'.format(name, desc, temp, ds, fl, ds, hum, ws)
        return label_text
    
    except:
        label_text = 'There was an error retrieving the data'
        return label_text

# Add weather icon to label
def open_image(icon):
    size = int(low_frame.winfo_height()*0.25)   # Return height of low_frame

    # Open icon resize and convert it to a tk image for label
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))

    # Remove any icons currently present
    weather_icon.delete("all")

    # Create new image on canvas and assign tk image created above
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


# Height & width for canvas
HEIGHT = 700
WIDTH = 800

root = tk.Tk()  # Create the main window
print(font.families())

# Top frame at top for text entry and button
# Lower frame for text response and weather icon

# Add canvas - rectangular container for drawing pictures and organizing layout
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Add background image
bg_image = tk.PhotoImage(file='landscape2.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add upper frame
top_frame = tk.Frame(root, bg='#80ccff', bd=5)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Add entry to upper frame
entry = tk.Entry(top_frame, font=('Ebrima', 20))
entry.place(relwidth=0.55, relheight=1)

# Add button to upper frame
# 1. Test the button
button = tk.Button(top_frame, text='Get Weather', font=('Ebrima', 22, 'bold'), command=lambda: get_weather(entry.get()))
button.place(relx=0.6, relwidth=0.4, relheight=1)   # Button is 25% of frame in width and height

# Add lower frame
low_frame = tk.Frame(root, bg='#80ccff', bd=10)
low_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Add label to lower frame
bg_color = '#f2f2f2'
label = tk.Label(low_frame, bg=bg_color, font=('Ebrima', 18), anchor='nw', justify='left', bd=5)
label.place(relwidth=1, relheight=1)    # Fill entire lower frame

# Add canvas for weather icon placement
weather_icon = tk.Canvas(label, bg='#dddddd', bd=0, highlightthickness=0)   # Gray background so the white icons are visible
weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)


root.mainloop()