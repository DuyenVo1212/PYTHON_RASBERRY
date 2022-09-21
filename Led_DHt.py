import RPi.GPIO as GPIO
import time
import board
import adafruit_dht
import psutil

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

LED_PIN_Gr = 2
LED_PIN_Ye = 3
LED_PIN_Re = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_Gr, GPIO.OUT)
GPIO.setup(LED_PIN_Ye, GPIO.OUT)
GPIO.setup(LED_PIN_Re, GPIO.OUT)

dhtDevice = adafruit_dht.DHT11(board.D26) 

while True:
    try:
        temp_c = dhtDevice.temperature
        temp_f = temp_c * (9 / 5) + 32
        humi = dhtDevice.humidity
        print("Temp: {}*F / {}*C    Humidity: {}% ".format(temp_f, temp_c, humi))
        if temp_c > 30:
            GPIO.output(LED_PIN_Re, GPIO.HIGH)
            time.sleep(1)
                
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1)
        continue
    
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)

GPIO.cleanup()

