#!/bin/python
#desc: Filter detection of persons using an image
#package:opencvodos

### Copyright(c) 2014 OpenDomo Services SL. Licensed under GPL v3 or later
import numpy as np
import cv2

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
        
if __name__ == '__main__':
    import sys
    from glob import glob
    import itertools as it

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
    
    for fn in it.chain(*map(glob, sys.argv[1:])):
      img = cv2.imread(fn)
      
