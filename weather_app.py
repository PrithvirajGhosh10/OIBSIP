import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "a1e14c65c2c6215521c390dd9aab0376"

# Function to get weather
def get_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=parameters)
    data = response.json()

    if data["cod"] == 200:

        city_label.config(text="City : " + data["name"])

        temp_label.config(
            text="Temperature : " + str(data["main"]["temp"]) + " °C"
        )

        weather_label.config(
            text="Weather : " + data["weather"][0]["description"]
        )

        humidity_label.config(
            text="Humidity : " + str(data["main"]["humidity"]) + "%"
        )

        wind_label.config(
            text="Wind Speed : " + str(data["wind"]["speed"]) + " m/s"
        )

    else:
        messagebox.showerror("Error", "City not found!")

# Function to clear data
def clear():

    city_entry.delete(0, tk.END)

    city_label.config(text="City :")
    temp_label.config(text="Temperature :")
    weather_label.config(text="Weather :")
    humidity_label.config(text="Humidity :")
    wind_label.config(text="Wind Speed :")


# GUI
root = tk.Tk()

root.title("Weather App")

root.geometry("400x350")

title = tk.Label(root,
                 text="Weather App",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

city_entry = tk.Entry(root,
                      width=25,
                      font=("Arial", 12))
city_entry.pack(pady=10)

tk.Button(root,
          text="Get Weather",
          command=get_weather,
          bg="green",
          fg="white").pack()

city_label = tk.Label(root,
                      text="City :",
                      font=("Arial", 11))
city_label.pack(pady=5)

temp_label = tk.Label(root,
                      text="Temperature :",
                      font=("Arial", 11))
temp_label.pack(pady=5)

weather_label = tk.Label(root,
                         text="Weather :",
                         font=("Arial", 11))
weather_label.pack(pady=5)

humidity_label = tk.Label(root,
                          text="Humidity :",
                          font=("Arial", 11))
humidity_label.pack(pady=5)

wind_label = tk.Label(root,
                      text="Wind Speed :",
                      font=("Arial", 11))
wind_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(button_frame,
          text="Clear",
          command=clear,
          width=10).grid(row=0, column=0, padx=5)

tk.Button(button_frame,
          text="Exit",
          command=root.destroy,
          width=10).grid(row=0, column=1, padx=5)

root.mainloop()