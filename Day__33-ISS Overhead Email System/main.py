'''
ISS Overhead Email System
- Check if the ISS satellite is overhead the desired location (plus minus 5 degrees error of margin in latitude and longitude)
- If it does and it is night time, send an email
'''

import smtplib  #SMTP libraray
import time

import requests
from datetime import datetime

MY_EMAIL = "myemail.gmail.com"
MY_PASSWORD = "my_password"
ISS_overhead = False
Night_time = False

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_iss_overhead():
    '''Function that request data from iss api and checking if the iss is near my position
    response : request object
        data from "http://api.open-notify.org/iss-now.json"
    iss_latitude : float
        latitude of iss position
    iss_longtitude: float
        longitude of iss position
    '''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    '''Function that if it is currently nightime
    response : request object
        data from "https://api.sunrise-sunset.org/json"
    sunrise : int
        hour of sunrise
    sunset : int
        hour of sunset
    '''
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, #24 hours format
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour #getting the current hour

    #if the current hour is within the sunset and sunrise, return True for night time
    if time_now >= sunset or time_now <= sunrise:
        return True

#Continously loop while True
while True:
    time.sleep(60) #time sleep for 60 seconds
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up\n\nThe ISS is above you in the sky"

        )





