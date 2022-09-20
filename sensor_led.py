import Adafruit_DHT as dht ## thêm thư viện Adafruit để đọc dữ liệu từ cảm biến
import RPi.GPIO as GPIO
import time


sensor = dht.DHT11 ##chọn loại cảm biến dht11

GPIO.setmode(GPIO.BCM) ##chọn chế độ chân cắm BCM

pin_sensor = 14 ## chân nhận data từ sensor là 14

LED_GREEN = 15 ## Gắn chân GPIO so 15 cho den xanh
LED_YELLOW = 18 ## Gắn chân GPIO so 18 cho den vang
LED_RED = 23 ## Gắn chân GPIO so 23 cho den do

GPIO.setwarnings(False) 

GPIO.setup(LED_GREEN, GPIO.OUT) ## Dat che do out cho den xanh
GPIO.setup(LED_YELLOW, GPIO.OUT) ## Dat che do out cho den vang
GPIO.setup(LED_RED, GPIO.OUT) ## Dat che do out cho den do

while(1):
    time.sleep(2) ## Dung 2 giay moi lan doc du lieu tu cam bien
    hum, temp = dht.read_retry(sensor, pin_sensor) # doc du lieu tu cam bien
    print("Humidity: ", hum, "Temp: ",  temp) # in ra du lieu nhiet do, do am
    if(temp > 25): ## Tren 25 do thi den do bat
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)
    if(temp <= 25 and temp > 20): ## Duoi 25 va tren 20 do thi den vang bat
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        GPIO.output(LED_GREEN, GPIO.LOW)
    if(temp <= 20): ## Duoi 20 do thi den xanh bat
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.HIGH)
    