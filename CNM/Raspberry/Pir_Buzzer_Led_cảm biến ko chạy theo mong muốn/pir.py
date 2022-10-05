import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
#xác định chân GPIO PIR_PIN làm đầu vào
try:
	print("Kiểm tra mô-đun PIR (CTRL + C để thoát)")
	time.sleep(2)
	print("Ready")
	while True:
#kiểm tra trạng thái đầu vào của PIR_PI,sử dụng câu lệnh True chạy trên một vòng lặp vô hạn.
		if GPIO.input(PIR_PIN):
			print("Đã phát hiện chuyển động! ",time.asctime(time.gmtime()))
		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
