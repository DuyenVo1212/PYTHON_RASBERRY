import RPi.GPIO as GPIO # su dung thu vien 
import time #thu vien thoi gian
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
#GPIO.setup(14,GPIO.OUT)
while(True):
	GPIO.output(18,GPIO.HIGH)
	print('ON')
	time.sleep(1)#second
	GPIO.output(18, GPIO.LOW)
	print('OFF')
	time.sleep(1)
	#GPIO.output(18,False)
	#GPIO.output(14,True)
	#print('OFF')
	#time.sleep(0.5)
                                                         
