import numpy as np
import cv2
# This Code would take input from your webcam and then flip the feed and disply it back.

cap = cv2.VideoCapture(0)

while(True):
	ret ,frame = cap.read()
	frame = cv2.flip(frame,0)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break

#WHEN everything done , release the capture
cap.release()
cv2.destroyAllWindows()
