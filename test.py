INTERVAL = 5
COUNT = 1080

import time
import picamera

import os
import datetime

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
	os.system(f"mkdir -p /home/pi/data/{datetime.datetime.now().strftime('%F')}")

	start = time.time()
	for count, filename in enumerate(camera.capture_continuous("/home/pi/data/{timestamp:%F}/{timestamp:%T}.jpeg", format="jpeg", resize=(640, 480))):
		os.system(f"mkdir -p /home/pi/data/{datetime.datetime.now().strftime('%F')}")
		os.system("sync")
		if count == COUNT-1:
			break

		end = time.time()
		time.sleep(INTERVAL - (end - start))
		start = time.time()
