'''
ISS API program
- To find out the current position of the ISS satellite at the current time
return: (longitude, latitude)
'''

import requests #import requests module
from datetime import datetime

MY_LAT = 1.297588
MY_ING = 103.854309

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_postion = (longitude,latitude)
print(iss_postion)


