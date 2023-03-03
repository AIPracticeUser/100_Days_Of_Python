'''
Sunrise and Sunset API program
- To find out the Sunrise and Sunset timing given the latitude and longitude
- return: Datetime Object
'''

import requests #import requests module
from datetime import datetime

MY_LAT = 1.297588
MY_ING = 103.854309

parameters = {
    "lat": MY_LAT,
    "lng": MY_ING,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f'Sunrise time: {sunrise}')
print(f'Sunset time: {sunset}')

time_now = datetime.now()
print(f'Hour time now is : {time_now.hour}')