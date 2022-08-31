import pyfirmata
led_pin = 8
board = pyfirmata.Arduino("/dev/ttyACM0")
print('Code is running')
while True:
	board.digital[led_pin].write(0)
	board.pass_time(2)
	board.digital[led_pin].write(1)
	board.pass_time(2)
