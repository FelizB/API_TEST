from datetime import datetime
import time
import smtplib
import requests
import API

my_email = "email.gmail.com"
password = "gffdwpwvurpjizwt"

data = list(API.ISS())
long = float(data[1])
lat = float(data[0])

# My location
MY_LAT = 51.587351
MY_LONG = -0.127758


def is_iss_overhead():
    if MY_LAT-5 <= lat <= MY_LAT+5 and MY_LONG-5 <= long <= MY_LONG+5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise = int((response.json()["results"]["sunrise"]).split("T")[1].split(":")[0])
    sunset = int((response.json()["results"]["sunset"]).split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            # hotmail = "smtp.live.com" yahoo="smtp.mail.com"
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="email@gmail.com",
                                msg=f"Subject:Look up \n\nThe ISS is above you in the sky")

