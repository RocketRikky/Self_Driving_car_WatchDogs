import numpy as np
from mss import mss 
import cv2
import time

sct = mss()

def process_img(image):
	processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
	return processed_img



last_time = time.time()
while(True):
	bbox = {'top':0, 'left':40, 'width':800, 'height':600}
	screen = np.array(sct.grab(bbox))
	new_screen = process_img(screen)

	print("Loop took {} seconds".format(time.time()-last_time))
	last_time = time.time()

	cv2.imshow('window', new_screen)

#	cv2.imshow('window2',cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))

	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break