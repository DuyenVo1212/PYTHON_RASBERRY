from picamera import PiCamera
import time
camera = PiCamera()
camera.start_preview()
print("Hello")