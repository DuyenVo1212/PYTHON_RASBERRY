import RPi.GPIO as GPIO
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if temperature >= 28:
		GPIO.output(18,True)		
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
	else:
		print("Failed to retrieve data from humidity sensor")
