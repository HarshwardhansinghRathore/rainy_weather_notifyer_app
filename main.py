import requests
import smtplib
import os

account_sid = 'ACc20f45269d1779c327a4a18be6e85c5e'
auth_token = 'c847d9fa184084207cc955afd2244c4d'

APIkey = '1d82f6660736dfe232894b5c27f3cd8a'
lat = 26.283340
lon = 73.021858

response = requests.get(url=f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}'
                            f'&exclude=current,minutely,daily&appid={APIkey}')
response.raise_for_status()
weather_data = response.json()
is_raining = False

for weather in weather_data['hourly'][0:12]:
    weather_code = weather['weather'][0]['id']
    if weather_code < 622:
        is_raining = True

if is_raining:
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user='hr1566027@gmail.com', password=os.environ['PASSWORD'])
    connection.sendmail(from_addr='hr1566027@gmail.com', to_addrs='hr32602@gmail.com',
                        msg="Subject:Weather report\n\nhello harsh singh rathore hope you are having a good day if you are planing to go out side you "
                            "better take a umbrella with you"
                        )
