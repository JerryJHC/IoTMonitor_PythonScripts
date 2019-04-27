# importing the requests library 
import requests
import subprocess
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

# defining the firebase-endpoint 
API_ENDPOINT = "https://us-central1-iotmonitor-9c57a.cloudfunctions.net/save"

#CPU Heat
cpu = subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True)
cpu = int(cpu)/1000

#Average temperature
avgTemperature = (sense.get_temperature_from_humidity() + sense.get_temperature_from_pressure()) / 2

#Calculate temperature
temperature = avgTemperature - ( cpu - avgTemperature )

# data to be sent to firebase
data = {"temperature": temperature, 
		"humidity": sense.get_humidity(), 
		"pressure": sense.get_pressure()} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data=data)

# extracting response text 
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 
print("Time: %s"%str(datetime.now()))
print("Saved values: ")
print(data)
print("------------------------------------------------")