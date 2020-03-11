import time
import picamera

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

	camera.capture_sequence([f"image{i}.png" for i in range(10)])
