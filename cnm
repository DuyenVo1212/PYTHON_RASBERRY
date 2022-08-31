import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
def MOTION(PIR_PIN):
	print('Motion Detected!')
#---------------------------------
print('PIR Module Test (CTRL+C to exit)')
time.sleep(2)
print('Ready')
try:
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
	while 1:
		time.sleep(100)
except KeyboardInterrupt:
	print(' Quit')
	GPIO.cleanup()import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	
#    if humidity is not None and temperature is not None:
	print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
#    else:
#        print("Failed to retrieve data from humidity sensor")
#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_1.py
# Measure distance using an ultrasonic module
#
# Ultrasonic related posts:
# http://www.raspberrypi-spy.co.uk/tag/ultrasonic/
#
# Author : Matt Hawkins
# Date   : 16/10/2016
# -----------------------

# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# Speed of sound in cm/s at temperature
temperature = 20
speedSound = 33100 + (0.6*temperature)

print("Ultrasonic Measurement")
print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
solan=1
sum=0
while (solan <=10):   #kiểm tra 5 lần
	# Set trigger to False (Low)
	GPIO.output(GPIO_TRIGGER, False)
	# Allow module to settle
	time.sleep(0.5)
	# Send 10us pulse to trigger
	GPIO.output(GPIO_TRIGGER, True)
	# Wait 10us
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start = time.time()
	while GPIO.input(GPIO_ECHO)==0:
		start = time.time()
	while GPIO.input(GPIO_ECHO)==1:
		stop = time.time()
	# Calculate pulse length
	elapsed = stop-start
	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * speedSound
	# That was the distance there and back so halve the value
	distance = distance / 2
	print("Khoảng cách đo lần ",solan," : {0:5.1f}".format(distance))
	sum=sum + distance
	solan =solan + 1
	time.sleep(0.5)
khoangcach = sum / 10
print("Distance trung bình: {0:5.4f}".format(khoangcach))
#print("Distance trung bình : {0:5.1f}".format(distance))
# Reset GPIO settings
GPIO.cleanup()#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_1.py
# Measure distance using an ultrasonic module
#
# Ultrasonic related posts:
# http://www.raspberrypi-spy.co.uk/tag/ultrasonic/
#
# Author : Matt Hawkins
# Date   : 16/10/2016
# -----------------------

# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# Speed of sound in cm/s at temperature
temperature = 20
speedSound = 33100 + (0.6*temperature)

print("Ultrasonic Measurement")
print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
solan=1
sum=0
while (solan <=8):   #kiểm tra 8 lần
	# Set trigger to False (Low)
	GPIO.output(GPIO_TRIGGER, False)
	# Allow module to settle
	time.sleep(0.5)
	# Send 10us pulse to trigger
	GPIO.output(GPIO_TRIGGER, True)
	# Wait 10us
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start = time.time()
	while GPIO.input(GPIO_ECHO)==0:
		start = time.time()
	while GPIO.input(GPIO_ECHO)==1:
		stop = time.time()
	# Calculate pulse length
	elapsed = stop-start
	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * speedSound
	# That was the distance there and back so halve the value
	distance = distance / 2
	print("Khoảng cách đo lần ",solan," : {0:5.1f}".format(distance),"cm")
	sum=sum + distance
	solan =solan + 1
	time.sleep(0.5)
khoangcach = sum / 8
print("Distance trung bình: {0:5.4f}".format(khoangcach),"cm")
#print("Distance trung bình : {0:5.1f}".format(distance))
# Reset GPIO settings
GPIO.cleanup()
import Adafruit_DHT as dht
#import sys
from urllib.request import urlopen
from time import sleep
DHT_SENSOR = dht.DHT11
DHT_PIN = 4
#Enter Your API key
myAPI = "XEIU8767B7E5RSS6" 
baseURL = 'https://api.thingspeak.com/update?api_key=%s'%myAPI
#-----------------------------------
def DHT_data():
	humi,temp = dht.read_retry(DHT_SENSOR,DHT_PIN)
	return humi, temp
#------------------------------------
while True:
	humi, temp = DHT_data()
	print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temp, humi))
	if isinstance(humi,float) and isinstance(temp,float):
		humi = '%.2f' % humi
		tem = '%.2f' % temp
	#print(tem,humi)
	#send the data to thingspeak
		conn = urlopen(baseURL+'&field1=%s&field2=%s' % (temp, humi))
		print(conn.read)
	#closing the connection
		conn.close()
	else:
		print('Error')
	sleep(0.5)
import serial
import RPi.GPIO as GPIO
import time
print('hello')
ser=serial.Serial("/dev/ttyACM1",9600)
ser.baudrate=9600
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
	return
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
while True:
	read_ser = ser.readline()
	print(read_ser)
	if (read_ser == "Hello From Arduino!"):
		blink(13)import RPi.GPIO as GPIO # su dung thu vien 
import time #thu vien thoi gian
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12,GPIO.OUT)
while(True):
	GPIO.output(18,True)
	time.sleep(0.5)
	GPIO.output(18,False)
	time.sleep(0.5)
# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming
#Web Browser : <IP Address>:8000/index.html
import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server

PAGE="""\
<html>
<head>
<title>Raspberry Pi - Surveillance Camera</title>
</head>
<body>
<center><h1>Raspberry Pi - Surveillance Camera</h1></center>
<center><img src="stream.mjpg" width="640" height="480"></center>
</body>
</html>
"""

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 90
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
while True:
	i=GPIO.input(11)
	if i == 0:
		print("No intruders  ",i)
		GPIO.output(3,0)
		time.sleep(0.1)
	elif i == 1:
		print("Intruder detected ",i)
	GPIO.output(3,1)
	time.sleep(0.1)

import pyfirmata
led_pin = 8
board = pyfirmata.Arduino("/dev/ttyACM0")
print('Code is running')
while True:
	board.digital[led_pin].write(0)
	board.pass_time(2)
	board.digital[led_pin].write(1)
	board.pass_time(2)
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
try:
	print("PIR Module Test (CTRL+C to exit)")
	time.sleep(2)
	print("Ready")
	while True:
		if GPIO.input(PIR_PIN):
			#td=t()
			print("Motion Detected! ",time.asctime(time.gmtime()))
		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_1.py
# Measure distance using an ultrasonic module
#
# Ultrasonic related posts:
# http://www.raspberrypi-spy.co.uk/tag/ultrasonic/
#
# Author : Matt Hawkins
# Date   : 16/10/2016
# -----------------------

# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# Speed of sound in cm/s at temperature
temperature = 20
speedSound = 33100 + (0.6*temperature)

print("Ultrasonic Measurement")
print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
time.sleep(0.5)

# Send 10us pulse to trigger
GPIO.output(GPIO_TRIGGER, True)
# Wait 10us
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)
start = time.time()

while GPIO.input(GPIO_ECHO)==0:
  start = time.time()

while GPIO.input(GPIO_ECHO)==1:
  stop = time.time()

# Calculate pulse length
elapsed = stop-start
print('Thời gian gặp vật cản  :',elapsed)
# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
distance = elapsed * speedSound

# That was the distance there and back so halve the value
distance = distance / 2

print("Distance : {0:5.1f}".format(distance))

# Reset GPIO settings
GPIO.cleanup()import RPi.GPIO as GPIO
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


host_name = '169.254.91.19'    # Change this to your Raspberry Pi IP address
host_port = 8000


class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command 
            'curl -I http://server-ip-address:port' 
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command 
            'curl http://server-ip-address:port' 
        """
        html = '''
            <html>
            <body style="width:960px; margin: 20px auto;">
            <h1>Welcome to DHCNTT15AVL</h1>
            <p>Current GPU temperature is {}</p>
            <form action="/" method="POST">
                Turn LED1 :
                <input type="submit" name="submit" value="On1">
                <input type="submit" name="submit" value="Off1">
		Turn LED2 :
                <input type="submit" name="submit" value="On2">
                <input type="submit" name="submit" value="Off2">
            </form>
            </body>
            </html>
        '''
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):
        """ do_POST() can be tested using curl command 
            'curl -d "submit=On" http://server-ip-address:port' 
        """
        content_length = int(self.headers['Content-Length'])    # Get the size of data
        post_data = self.rfile.read(content_length).decode("utf-8")   # Get the data
        post_data = post_data.split("=")[1]    # Only keep the value
        
        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)

        if post_data == 'On1':
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)
        print("LED is {}".format(post_data))
        self._redirect('/')    # Redirect back to the root url
if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()#!/usr/bin/env python
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
import RPi.GPIO as GPIO
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if temperature >= 32:
		GPIO.output(18,True)		
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
	else:
		print("Failed to retrieve data from humidity sensor")
import RPi.GPIO as GPIO # su dung thu vien 
import time #thu vien thoi gian
GPIO.setmode(GPIO.BCM) # 
GPIO.setup(18,GPIO.OUT)
while(True):
	GPIO.output(18,True)
	time.sleep(0.5)
	GPIO.output(18,False)
	time.sleep(0.5)
import RPi.GPIO as GPIO
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if temperature >= 32:
		GPIO.output(18,True)		
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
	else:
		print("Failed to retrieve data from humidity sensor")
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
camera = PiCamera()
camera.rotation = 180
camera.start_preview()
GPIO.setup(PIR_PIN, GPIO.IN)
print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print("Ready")
while True:
	if GPIO.input(PIR_PIN):
		print("Motion Detected! ",time.asctime(time.gmtime()))
		camera.capture('/home/pi/Desktop/image.jpg')
		print("A photo has been taken at ",time.asctime(time.gmtime()))
		camera.stop_preview()
		exit()#thoat khoi CT

import RPi.GPIO as GPIO
import time
from picamera import PiCamera
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
camera = PiCamera()
camera.rotation = 180
camera.start_preview()
GPIO.setup(PIR_PIN, GPIO.IN)
try:
	print("PIR Module Test (CTRL+C to exit)")
	time.sleep(2)
	print("Ready")
	while True:
		if GPIO.input(PIR_PIN):
			#td=t()
			print("Motion Detected! ",time.asctime(time.gmtime()))
			camera.capture('/home/pi/Desktop/image.jpg')
			print("A photo has been taken")
			camera.stop_preview()
			exit()
		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
import Adafruit_DHT as dht
#import sys
from urllib.request import urlopen
from time import sleep
DHT_SENSOR = dht.DHT11
DHT_PIN = 4
#Enter Your API key
myAPI = "J10OSBIQTWBSFROB"
#myAPI = "XEIU8767B7E5RSS6" 
baseURL = 'https://api.thingspeak.com/update?api_key=%s'%myAPI
#-----------------------------------
def DHT_data():
	humi,temp = dht.read_retry(DHT_SENSOR,DHT_PIN)
	return humi, temp
#------------------------------------
while True:
	humi, temp = DHT_data()
	print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temp, humi))
	if isinstance(humi,float) and isinstance(temp,float):
		humi = '%.2f' % humi
		tem = '%.2f' % temp
	#print(tem,humi)
	#send the data to thingspeak
		conn = urlopen(baseURL+'&field1=%s&field2=%s' % (temp, humi))
		print(conn.read)
	#closing the connection
		conn.close()
	else:
		print('Error')
	sleep(0.5)
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	
#    if humidity is not None and temperature is not None:
	print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
#    else:
#        print("Failed to retrieve data from humidity sensor")
#Project 13 - Burglar Detector With Photo Capture
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause

#create objects that refer to a button,
#a motion sensor and the PiCamera
button = Button(2)
pir = MotionSensor(4)
camera = PiCamera()

#start the camera
camera.rotation = 180
camera.start_preview()

#image image names
i = 0

#stop the camera when the pushbutton is pressed
def stop_camera():
    camera.stop_preview()
    #exit the program
    exit()

#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    camera.capture('/home/pi/Desktop/image_%s.jpg' % i)
    print('A photo has been taken')
    sleep(10)

#assign a function that runs when the button is pressed
button.when_pressed = stop_camera
#assign a function that runs when motion is detected
pir.when_motion = take_photo

pause()
import serial
import RPi.GPIO as GPIO
import time
print('hello')
ser=serial.Serial("/dev/ttyACM1",9600)
ser.baudrate=9600
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
	return
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
while True:
	read_ser = ser.readline()
	print(read_ser)
	if (read_ser == "Hello From Arduino!"):
		blink(13)#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_1.py
# Measure distance using an ultrasonic module
#
# Ultrasonic related posts:
# http://www.raspberrypi-spy.co.uk/tag/ultrasonic/
#
# Author : Matt Hawkins
# Date   : 16/10/2016
# -----------------------

# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# Speed of sound in cm/s at temperature
temperature = 20
speedSound = 33100 + (0.6*temperature)

print("Ultrasonic Measurement")
print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
time.sleep(0.5)

# Send 10us pulse to trigger
GPIO.output(GPIO_TRIGGER, True)
# Wait 10us
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)
start = time.time()

while GPIO.input(GPIO_ECHO)==0:
  start = time.time()

while GPIO.input(GPIO_ECHO)==1:
  stop = time.time()

# Calculate pulse length
elapsed = stop-start
print('Thời gian gặp vật cản  :',elapsed)
# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
distance = elapsed * speedSound

# That was the distance there and back so halve the value
distance = distance / 2

print("Distance : {0:5.1f}".format(distance))

# Reset GPIO settings
GPIO.cleanup()