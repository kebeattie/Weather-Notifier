import requests
import json
from win10toast import ToastNotifier
from dotenv import load_dotenv
import os

load_dotenv()

#n = ToastNotifier()
status = 0

def getWeather (city = "Liverpool"):
    lat = None
    lon = None

    #
        

    sitelist = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=" + city.title() + "&limit=1&limit=1&appid="+os.getenv("API_KEY")) # Retrieves JSON site lat and lon
        
       
    
    list = sitelist.json() # Puts data from API call into json object

    try:
        lat = str((list[0]["lat"]))
        lon = str((list[0]["lon"])) #extracts lat and lon from json. To be passed into next API call
    except: 
        
         print ("\nLocation not found\n")
#        city = input("Enter your location: ")
            

    response_API = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=" + lat +"&lon=" + lon +"&units=metric&exclude=minutely,hourly,daily,alerts&appid="+os.getenv("API_KEY")) # Requests weather data for user specified location
    #status = sitelist.status_code
        
    
    weatherData = response_API.json() # Puts data from API call into json object
    
    return weatherData

def getStatus():
    return status
    
status = getStatus()
    
if __name__ == "__main__":
    
    city = input("Enter your location: ")

    data = getWeather(city)
    
    

    #currentTemp = (data["current"]["temp"]) # Extracts current temp from json

    #condition = (data["current"]["weather"][0]["description"]) # Extracts current condtion from json

#result = "Current Temp = " + str(currentTemp) + "°C\n" + "Condition = " + condition.title() # Puts all releveant information into string to be passed into notification

#n.show_toast(userInput.title() + " Current Weather", result, duration = 10) # Sends notification