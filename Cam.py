import numpy as np
import time
import argparse
import imutils
import cv2

# Define the upper and lower boundaries of the "green" object in the HSV color space
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Allow the camera to warm up
time.sleep(2.0)

# Initialize the background image
background = None

# Loop over frames from the webcam
while True:
	# Read the current frame from the webcam
	_, frame = cap.read()

	# Resize the frame and convert it to grayscale
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Blur the frame to reduce high frequency noise
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# If the background image is None, initialize it
	if background is None:
		background = gray
		continue

	# Compute the absolute difference between the current frame and the background
	diff = cv2.absdiff(background, gray)

	# Threshold the difference image to identify pixels above a certain value
	thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

	# Dilate the thresholded image to fill in holes
	thresh = cv2.dilate(thresh, None, iterations=2)

	# Find contours in the thresholded image
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	# Loop over the contours
	for c in cnts:
		# If the contour is too small, ignore it
		if cv2.contourArea(c) < 500:
			continue

		# Compute the bounding box for the contour and draw it on the frame
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# Show the frame
	cv2.imshow("Frame", frame)

	# If the 'q' key is pressed, break from the loop
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()