from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # Weather API
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=18d23d194b33b12ccd96f5595f24f642"

    json_data = requests.get(api).json()
    try:
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | FEELS LIKE {temp}°C")
        w.config(text=f"Wind Speed: {wind} m/s")
        h.config(text=f"Humidity: {humidity}%")
        d.config(text=f"Description: {description}")
        p.config(text=f"Pressure: {pressure} hPa")
    except KeyError:
        messagebox.showerror("Error", "City not found!")

# Search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="grey83", borderwidth=0, highlightthickness=0, fg="black")
textfield.place(x=80, y=42)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, highlightthickness=0, cursor="hand2", command=getWeather)
myimage_icon.place(x=390, y=42)

# Logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=170, y=110)

# Bottom box
Frame_image = PhotoImage(file="banner.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", highlightthickness=0, bg="deep sky blue")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Labels for Weather Information
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)
w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="black")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="black")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="black")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="black")
p.place(x=670, y=430)

root.mainloop()
