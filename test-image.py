import cv2 
import numpy as np

bg_path = "images/background/0.jpg"
fg_path = "images/objects/obj1/sample2.jpg"
img_w_path = "images/render/result1.jpg"

bg = cv2.imread(bg_path)
fg= cv2.imread(fg_path)

fg_grayscale = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY) 
fg_grayscale = cv2.resize(fg_grayscale, )

## use 3 options, threasholding, color(HSV) and polygon 

# method 1
# threshold 
_, mask_th = cv2.threshold(fg_grayscale, 100, 255, cv2.THRESH_BINARY)


#method2 
# mask poly
mask_poly = np.zeros(fg_grayscale.shape[:2], dtype=np.uint8)
points = np.array([[10,50], [100,300], [400,200], [50,100]], dtype=np.int32)
cv2.fillPoly(mask_poly, [points], 255)

cv2.imshow("gray", fg_grayscale)
cv2.imshow("mask th", mask_th)
cv2.imshow("mask poly", mask_poly)

cv2.waitKey(0)
#fin_image = cv2.add(bg, fg)

