INTERVAL = 5

import time
import picamera
import os

with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	camera.framerate = 30
	time.sleep(2)
	camera.shutter_speed = camera.exposure_speed
	camera.exposure_mode = "off"
	g = camera.awb_gains
	camera.awb_mode = "off"
	camera.awb_gains = g
	print("done")
	os.system("mkdir -p /home/pi/data/${date +%F}")

	start = time.time()
	for filename in camera.capture_continous("/home/pi/data/${date +%F}/$(date +%T).jpg", format="jpg", resize=(640, 480)):
		end = time.time()
		time.sleep(INTERVAL - (end - start))
		start = time.time()
