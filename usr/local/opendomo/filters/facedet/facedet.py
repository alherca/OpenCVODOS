#!/bin/python
#desc: Motion detection filter using an image
#package:opencvodos

### Copyright(c) 2014 OpenDomo Services SL. Licensed under GPL v3 or later

import sys
import cv2
import time
import ConfigParser
import numpy as np
import subprocess

IDC=sys.argv[1]

# Read parameters or arguments
config = ConfigParser.ConfigParser()
config.read('/etc/opendomo/vision/' + IDC + '/filters/facedet.conf')
confID = config.get('Definition', 'ID')
confNAME = config.get('Definition', 'NAME')

#Only developer
#print confID
#print confNAME

# Load image
img = cv2.imread('/var/www/data/' + confID + '.jpg')



# save log
subprocess.call(["/bin/logevent", "facedet", "opencvodos", "detection of faces in " + confID +  " /var/www/data/" + confID + "_facedet.png"])
# save output image
cv2.imwrite('/var/www/data/' + confID + '_facedet.png',img)
