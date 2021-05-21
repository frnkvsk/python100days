import time

import requests
from datetime import datetime
import smtplib

MY_GOOGLE = "@gmail.com"
SMTP_GMAIL = "smtp.gmail.com"
MY_GOOGLE_PW = ""
MY_LATITUDE = 47.606209
MY_LONGITUDE = -122.332069


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LONGITUDE - 5 >= iss_longitude <= MY_LONGITUDE + 5 and MY_LATITUDE - 5 >= iss_latitude <= MY_LATITUDE + 5


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return sunrise >= time_now >= sunset


while True:
    global time_now
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(SMTP_GMAIL)
        connection.starttls()
        connection.login(MY_GOOGLE, MY_GOOGLE_PW)
        connection.sendmail(
            from_addr=MY_GOOGLE,
            to_addrs=MY_GOOGLE,
            msg=f"Subject:Look up\n\nThe ISS is above you in the sky!\nTime now:{time_now}"
        )
        print(time_now)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
print("sunrise ",sunrise)
print("sunset ",sunset)
print("iss_latitude ",iss_latitude)
print("iss_longitude ",iss_longitude)



