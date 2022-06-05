# ISS Tracker

##### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)

---


## Description

This app tracks the International Space Station and emails the user when the ISS should be visible to them.

##### Controls

- replace MY_EMAIL value with the email account you wish to mail both from and to
    - to email from an account that is not a gmail account the SMTP_HOST value will need to be updated 
        - SMTP Information
                       gmail         hotmail             yahoo
             host  smtp.gmail.com  smtp.live.com     smtp.mail.yahoo.com
- replace MY_PASSWORD value with the valid password for the email account you wish to mail from
- use [Latitude and Longitude Finder](#latitude-and-longitude-finder) to find the coordinates of the location you wish to monitor
    - replace the values of MY_LAT and MY_LONG with the latitude and longitude coordinates provided by the site



##### Technologies

- Python
- API requests
- smtplib
- Visual Studio

---

## How To Use

Download or clone this repository to your desktop. Run main.py in an appropriate Python environment. This app must be left running in order to monitor the station and report to the user.

---

## References

##### Latitude and Longitude Finder
- https://www.latlong.net/

##### Continuing Work on

- https://github.com/SDBranka/_100DOP_Exercises

\
[Back To The Top](#iss-tracker)