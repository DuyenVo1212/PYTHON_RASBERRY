#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sudo apt-get update
#sudo apt-get install python3-dev libmariadb-dev-compat libmariadb-dev
#sudo pip3 install mysqlclient
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT
import MySQLdb
import datetime

#conn = MySQLdb.connect(host= "localhost",user= "***",passwd=***",db="readings")
conn = MySQLdb.connect(host= "localhost",user= "admin",passwd="123456",db="readings")

c=conn.cursor()

def dhtreading_witesql():

     sensor_args = { '11': Adafruit_DHT.DHT11,
                                '22': Adafruit_DHT.DHT22,
                                '2302': Adafruit_DHT.AM2302 }
     if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
                                sensor = sensor_args[sys.argv[1]]
                                pin = sys.argv[2]
     else:
                                print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
                                print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
                                sys.exit(1)

     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

     if humidity is not None and temperature is not None:
                               print('Temperature={0:0.1f}°C Humidity={1:0.1f}%'.format(temperature, humidity))
     else:
                               print('Failed to get reading. Try again!')
                               sys.exit(1)

     unix = int(time.time())
     date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

     c.execute("INSERT INTO tempdata (Data, Temperatura, Umidita) VALUES (%s, %s, %s)",(date, temperature, humidity))

     conn.commit()

for i in range(1):
     dhtreading_witesql()

c.close
conn.close()
