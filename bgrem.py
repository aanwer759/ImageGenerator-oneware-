import cv2
import numpy as np
# Load the image
image = cv2.imread('images/objects/obj1/sample1.jpg') 
bg = cv2.imread("images/background/0.jpg")

# Convert to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Set threshold to detect non-black pixels
_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
# Create alpha channel with the inverted threshold
alpha_channel = cv2.bitwise_not(thresh)
# Add the alpha channel to the image
b,g,r = cv2.split(image)
rgba = b+g+r + [alpha_channel]
# Save the result
cv2.imshow('image_with_transparency.png', cv2.merge(r,g,b,[alpha_channel]))
cv2.waitKey(0)