import eel
import pyowm

owm = pyowm.OWM("cc9d3310396c390b0af73e093a6b66e0")

eel.init("web")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    a = "В городе " + place + " сейчас " + str(temp) + " градусов!"
    return a

#get_weather('Нью-Йорк, США')

eel.start("main.html", size=(700, 700))