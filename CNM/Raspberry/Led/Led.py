import RPi.GPIO as GPIO
import time

LED_PIN_Gr = 2
LED_PIN_Ye = 3
LED_PIN_Re = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_Gr, GPIO.OUT)
GPIO.setup(LED_PIN_Ye, GPIO.OUT)
GPIO.setup(LED_PIN_Re, GPIO.OUT)

while True:
    GPIO.output(LED_PIN_Gr, GPIO.HIGH)
    GPIO.output(LED_PIN_Ye, GPIO.LOW)
    GPIO.output(LED_PIN_Re, GPIO.LOW)
    time.sleep(1)
    
    GPIO.output(LED_PIN_Ye, GPIO.HIGH)
    GPIO.output(LED_PIN_Gr, GPIO.LOW)
    GPIO.output(LED_PIN_Re, GPIO.LOW)
    time.sleep(1)
    
    GPIO.output(LED_PIN_Re, GPIO.HIGH)
    GPIO.output(LED_PIN_Gr, GPIO.LOW)
    GPIO.output(LED_PIN_Ye, GPIO.LOW)
    time.sleep(1)
    
GPIO.cleanup()
