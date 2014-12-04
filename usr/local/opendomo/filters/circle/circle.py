#!/bin/python
#desc:Filter circle detection using a webcam
#package:opencvodos

### Copyright(c) 2014 OpenDomo Services SL. Licensed under GPL v3 or later
import cv2
import sys
import time
import ConfigParser
import numpy as np
import subprocess


ID=sys.argv[1]

# Read parameters or arguments
config = ConfigParser.ConfigParser()
config.read('/etc/opendomo/vision/filters/' + ID + '/circle.conf')
confID = config.get('Definition', 'ID')
confNAME = config.get('Definition', 'NAME')
print confID
print confNAME

image = cv2.imread('/var/www/data/' + confID + '.jpg')

# Load the images
#image =cv2.imread('images.jpg')

output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# detect circles in the image
circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)
 
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	subprocess.call(["/bin/logevent", "motiondet", "opencvodos", "Motion detected in + confID +  /var/www/data/ + confID + _circle.png"])
	# logevent motiondet opencvodos "Motion detected in " + confID + " /var/www/data/" + confID + "_circle.png"
 
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	
	# save the output image
cv2.imwrite('/var/www/data/' + confID + '_circle.png',output)
 
	# show the output image only PC
#	cv2.imshow("output", np.hstack([image, output]))
#	cv2.waitKey(0)
