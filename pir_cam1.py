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
