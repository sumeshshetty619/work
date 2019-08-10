import cv2
import numpy as np
import time


while True:
	cam = cv2.VideoCapture(0)
	time.sleep(2)
	ret,frame = cam.read()
	cv2.imshow('webcam', frame)
	if cv2.waitKey(1)&0xFF == ord('q'):
		break
	time.sleep
cam.release()
cv2.destroyAllWindows()