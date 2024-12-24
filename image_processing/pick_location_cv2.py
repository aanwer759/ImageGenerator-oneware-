import cv2 
import numpy as np

point_x = 0
point_y = 0
selected = False

def pick(event,x,y,flag, param):
    global point_x 
    global point_y
    global selected
    if event == cv2.EVENT_LBUTTONDOWN:
          point_x = x
          point_y = y
          selected = True 

def pick_location_imp(img_path):
    # reading the image 
    img = cv2.imread(img_path) 
    cv2.namedWindow(winname="Select Position to Place Image")
    # setting mouse handler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('Select Position to Place Image', pick) 
    while True:
        cv2.imshow('Select Position to Place Image',img)
        key = cv2.waitKey(1)
        if key == ord('q') or selected == True:
            break
    
    cv2.destroyWindow("Select Position to Place Image")
    return point_x, point_y