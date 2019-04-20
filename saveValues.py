# importing the requests library 
import requests
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

# defining the firebase-endpoint 
API_ENDPOINT = "https://us-central1-iotmonitor-9c57a.cloudfunctions.net/save"

# data to be sent to firebase
data = {"temperature": sense.get_temperature(), 
		"humidity": sense.get_humidity(), 
		"pressure": sense.get_pressure(), 
		"datetime": datetime.now()} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response text 
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 
print("Saved values: ")
print(data)
print("------------------------------------------------")