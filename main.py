# Importing the modules
import cv2
import numpy as np

# Reading the image
image = cv2.imread('img_1.png')

# Applying the filter
blimg = cv2.blur(image, (5, 5))

# Showing the image
cv2.imshow('Original', image)
cv2.imshow('Blurred', blimg)

cv2.waitKey()
cv2.destroyAllWindows()
