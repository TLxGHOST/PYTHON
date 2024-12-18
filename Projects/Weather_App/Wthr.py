import requests 
import json
import pyttsx3 as p

engine = p.init('sapi5')
engine.runAndWait()

with  open('./Access_key.txt','r') as f:
    pss=f.read()

def weather(city):
    tr=f'http://api.weatherstack.com/current?access_key={pss}&query={city}'
    url=requests.get(tr)
    data=json.loads(url.text)
    # print(data)
    # print(type(data))
    try:
        x=data['request']
        y=data['location']
        z=data['current']
        return f'The weather in {y["name"]} is {z["weather_descriptions"][0]} and the temperature is {z["temperature"]} degree celcius and the humidity is {z["humidity"]} percent. Currently the wind speed is {z["wind_speed"]} km/h and the wind direction is {z["wind_dir"]}'
    except:
        return "Sorry! I can't find the weather of this city"
    
def speak(str):
    engine.say(str)
    engine.runAndWait()

if __name__ == '__main__':
    print("Hello you")
    while True:
        x=input("Enter the city name: ")
        if x=='z':
            exit()
        else:
            speak(weather(x))