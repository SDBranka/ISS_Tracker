import requests
import smtplib
import datetime
import time

SMTP_HOST = "smtp.gmail.com"
MY_EMAIL = "something@gmail.com"
MY_PASSWORD = "aaaaaaaa"
MY_LAT = 51.507351
MY_LONG = -0.127758


def iss_near():
    # get lang/long parameters from ISS API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_long = float(iss_data["iss_position"]["longitude"])
    # iss_lat = 51.507351
    # iss_long = -0.127758
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
            return True
    return False


def is_night():
    # set formatted to 0 to receive time date in unix time
    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
    response.raise_for_status()
    data = response.json()
    # access the hour value
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # print(f"sunrise: {sunrise}")
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now()
    current_hour = time_now.hour
    # print(f"current_hour: {current_hour}")
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    return False



# Bonus: run the code every 60 secs
while True:
    time.sleep(60)
    # if the ISS is close to the user's current position
    # and if it is currently dark
    if iss_near(MY_LAT, MY_LONG) and is_night():
            # send an email to notify the user
            with smtplib.SMTP(SMTP_HOST) as connection:
                # start transport layer security - encryption
                connection.starttls()
                # login to email
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                # send email
                connection.sendmail(from_addr=MY_EMAIL, 
                                    to_addrs=MY_EMAIL,
                                    # subject = "ISS Is Visible", \n\n breaks subject from body of the email
                                    msg="Subject:ISS Is Visible!!!\n\nThe International Space Station can be seen at your location now!"
                )








