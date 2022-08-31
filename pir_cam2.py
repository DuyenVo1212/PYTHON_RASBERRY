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

