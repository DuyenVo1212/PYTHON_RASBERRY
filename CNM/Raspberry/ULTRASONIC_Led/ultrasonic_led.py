import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 20
GPIO_ECHO = 21
LED_PIN_Gr = 2
LED_PIN_Ye = 3
LED_PIN_Re = 4

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(LED_PIN_Gr, GPIO.OUT)
GPIO.setup(LED_PIN_Ye, GPIO.OUT)
GPIO.setup(LED_PIN_Re, GPIO.OUT)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if dist>0 and dist <=10:
                GPIO.output(LED_PIN_Re, GPIO.HIGH)
                GPIO.output(LED_PIN_Ye, GPIO.LOW)
                GPIO.output(LED_PIN_Gr, GPIO.LOW)
                
            elif dist>10 and dist <=20:
                GPIO.output(LED_PIN_Ye, GPIO.HIGH)
                GPIO.output(LED_PIN_Gr, GPIO.LOW)
                GPIO.output(LED_PIN_Re, GPIO.LOW)
                
            else:
                GPIO.output(LED_PIN_Gr, GPIO.HIGH)
                GPIO.output(LED_PIN_Re, GPIO.LOW)
                GPIO.output(LED_PIN_Ye, GPIO.LOW)
                
            time.sleep(1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Quit")
        GPIO.cleanup()
