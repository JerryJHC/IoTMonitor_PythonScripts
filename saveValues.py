# importing the requests library 
import requests
import json
from sense_hat import SenseHat
from datetime import datetime

# Convert datetime to json serializable
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

sense = SenseHat()

# defining the firebase-endpoint 
API_ENDPOINT = "https://us-central1-iotmonitor-9c57a.cloudfunctions.net/save"

# data to be sent to firebase
data = {"temperature": sense.get_temperature(), 
		"humidity": sense.get_humidity(), 
		"pressure": sense.get_pressure(), 
		"datetime": datetime.now()} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data=json.dumps(data, cls=DateTimeEncoder), headers={'Content-Type': 'application/json'})

# extracting response text 
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 
print("Saved values: ")
print(data)
print("------------------------------------------------")