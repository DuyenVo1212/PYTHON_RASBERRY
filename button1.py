#!/usr/bin/python3
import RPi.GPIO as GPIO
import time#thu vien
GPIO.setmode(GPIO.BOARD)
btn_pin = 11
GPIO.setup(btn_pin,GPIO.IN)
previousStatus = None
try:
	while True:
		input = GPIO.input(btn_pin)
		if input == GPIO.LOW and previousStatus == GPIO.HIGH:
			print("Button pressed ",time.ctime())
		previousStatus = input
except KeyboardInterrupt:
	print("Exception: KeyboardInterrupt")
finally:
	GPIO.cleanup()


