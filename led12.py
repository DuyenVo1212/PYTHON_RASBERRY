import RPi.GPIO as GPIO
import time

PIN = 36

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)         #LED output pin

while True:
    GPIO.output(PIN, 0)  #Turn OFF LED
    time.sleep(1)
    GPIO.output(PIN, 1)  #Turn ON LED
    time.sleep(1)