import cv2 
import numpy as np

point_x = 0
point_y = 0


def pick(event,x,y,flag, param):
    global point_x 
    global point_y

    if event == cv2.EVENT_LBUTTONDOWN:
          point_x = x
          point_y = y

def pick_location_imp(img_path):
    # reading the image 
    img = cv2.imread(img_path) 
    cv2.namedWindow(winname="Image")
    cv2.imshow('Image', img) 
    # setting mouse handler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('Image', pick) 
    while True:
        cv2.imshow('Image',img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    
    cv2.destroyWindow("Image")
    return point_x, point_y