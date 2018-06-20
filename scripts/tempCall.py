#! /usr/bin/python3

import forecastio
from gpiozero import *
import datetime
from time import sleep

api_key = "a6b52582a65d6c72e1cfbee13be44635"
lat = 29.691078
lng = -95.494720
red_led = LED(17)
yel_led = LED(27)
whi_led = LED(22)
gre_led = LED(23)
blu_led = LED(24)
button = Button(14)

while True:
    button.wait_for_press()
    # current_time = datetime.datetime.now()
    # forecast = forecastio.load_forecast(api_key, lat, lng, time = current_time)
    forecast = forecastio.load_forecast(api_key, lat, lng)
    byHour = forecast.hourly()
    tempHigh = 0
    for hourData in byHour.data[:3]:
        print(hourData.time)
        print(hourData.summary)
        print(hourData.apparentTemperature)
        tempHigh += hourData.apparentTemperature
    tempHigh = (tempHigh)/3
    # byDay = forecast.daily()
    # print(byDay.data[0].time)
    # print(byDay.data[0].summary)
    # print(byDay.data[0].apparentTemperatureHigh)
    # tempHigh = byDay.data[0].apparentTemperatureHigh
    if tempHigh > 95:
        blu_led.on()
        sleep(0.1)
        gre_led.on()
        sleep(0.1)
        whi_led.on()
        sleep(0.1)
        yel_led.on()
        sleep(0.1)
        red_led.on()
        sleep(5)
        red_led.off()
        sleep(0.1)
        yel_led.off()
        sleep(0.1)
        whi_led.off()
        sleep(0.1)
        gre_led.off()
        sleep(0.1)
        blu_led.off()
    elif 95 >= tempHigh > 87:
        blu_led.on()
        sleep(0.1)
        gre_led.on()
        sleep(0.1)
        whi_led.on()
        sleep(0.1)
        yel_led.on()
        sleep(5)
        yel_led.off()
        sleep(0.1)
        whi_led.off()
        sleep(0.1)
        gre_led.off()
        sleep(0.1)
        blu_led.off()
    elif 87 >= tempHigh > 80:
        blu_led.on()
        sleep(0.1)
        gre_led.on()
        sleep(0.1)
        whi_led.on()
        sleep(5)
        whi_led.off()
        sleep(0.1)
        gre_led.off()
        sleep(0.1)
        blu_led.off()
    elif 80 >= tempHigh > 70:
        blu_led.on()
        sleep(0.1)
        gre_led.on()
        sleep(5)
        gre_led.off()
        sleep(0.1)
        blu_led.off()
    elif 70 > tempHigh:
        blu_led.on()
        sleep(5)
        blu_led.off()
    # sleep(90)
