# Importing the modules
import cv2


# Reading the image
# add your image name instead of 'image.png'
image = cv2.imread('image.png')

# Applying the filter
blimg = cv2.blur(image, (5, 5))

# Showing the image
cv2.imshow('Original', image)
cv2.imshow('Blurred', blimg)

cv2.waitKey()
cv2.destroyAllWindows()
