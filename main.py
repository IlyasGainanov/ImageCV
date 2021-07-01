import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("venv/_2016-05-12 11-30-07_0102_2R.JPG")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

upper = (35, 52, 163)
lower = (20, 10, 101)

mask = cv.inRange(hsv, lower, upper)

plt.imshow(mask)
plt.show()