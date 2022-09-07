1. LED flashes

import pyfirmata

led_pin = 8

board = pyfirmata.Arduino("/dev/ttyACM0")

while True:

board.digital[led_pin].write(0)

board.pass_time(1)

board.digital[led_pin].write(1)

board.pass_time(1)

2. LED fade in and out

import time

import pyfirmata

delay = 0.3

brightness = 0

board = pyfirmata.Arduino("/dev/ttyACM0")

led = board.get_pin('d:8:p')

while True:

# increase

for i in range(0, 10):

brightness = brightness + 0.1

print "Setting brightness to %s" % brightness

led.write(brightness)

board.pass_time(delay)

# decrease

for i in range(0, 10):

print "Setting brightness to %s" % brightness

led.write(brightness)

brightness = brightness - 0.1

board.pass_time(delay)
