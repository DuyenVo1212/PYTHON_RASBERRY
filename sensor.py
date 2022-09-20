import Adafruit_DHT as dht ## Thêm thư viện Adafruit để đọc dữ liệu từ sensor
import RPi.GPIO as GPIO
import time


sensor = dht.DHT11 ##chọn loại cảm biến dht11

GPIO.setmode(GPIO.BCM) ##chọn chế độ chân cắm BCM

pin_sensor = 14 ## chân nhận data từ sensor là 14


while(1):
    time.sleep(2) ## Dừng 2s mỗi lần đọc dữ liệu
    hum, temp = dht.read_retry(sensor, pin_sensor) ## đọc dữ liệu từ nhiệt độ
    print("Humidity: ", hum, "Temp: ",  temp) ## In ra màn hình nhiệt độ và độ ẩm
    
    