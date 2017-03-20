import requests
import random
import time

##APPID = '42c10cb3eeaa0000506fdcf32b494c82'
##windquery = {'q' : 'Ankara', 'APPID' : APPID }
##
##w = requests.post('http://api.openweathermap.org/data/2.5/weather', params=windquery)
##
##print w.text

newvalue = 0
windspeed = 7.0


while True:
    payload = 'windspeed,region=tr-center value=' + repr(windspeed)
    try:
        r = requests.post('http://dev.soyut.com:8086/write?db=mydb2', data=payload)
    except requests.exceptions.RequestException as e:
        print "Connection Error. Retrying - ", e
    print r.status_code,
    #    print r.url
    #    print r.text
    time.sleep(1)
    newvalue = windspeed + random.uniform(-0.20, 0.20)
    print newvalue,
    if (newvalue > 0.0 and newvalue < 25.0):
        windspeed = newvalue
    print windspeed
