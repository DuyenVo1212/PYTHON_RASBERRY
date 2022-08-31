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
		blink(13)