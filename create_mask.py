import cv2 
import numpy as np

#img = np.zeros((600,600), dtype = np.uint8)
drawing = False
points_x = []
points_y = []


def draw(event,x,y,flag,params):
    global drawing
    global points_x
    global points_y 
    # Check if the mouse event triggered is cv2.EVENT_LBUTTONDOWN
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        
    # Check if mouse is moving using cv2.EVENT_MOUSEMOVE 
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            
            points_x.append(x)
            points_y.append(y)
            #cv2.circle(img,(x,y),3,(0,0,355),-1)
            
    # Checking whether the Left button is up using cv2.EVENT_LBUTTONUP
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        points_x.append(x)
        points_y.append(y)
        #cv2.circle(img,(x,y),3,(0,0,255),-1)
  


def process_image(img_path, bg_image):
    global points_x
    global points_y
    points_x = []
    points_y = []
    # reading the image 
    scale_percent = 100
    img = cv2.imread(img_path)
    img_bg = cv2.imread(bg_image)
    bgh, bgw, _ =img_bg.shape
    imgh, imgw, _ = img.shape
    if (imgh>bgh) or (imgw > bgh): 
        scale_percent = 25
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)

    img = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
    # displaying the image 
    cv2.namedWindow(winname="Image")
  
    # setting mouse handler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('Image', draw) 
    while True:
        cv2.imshow('Image',img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

  
    # close the window 
    cv2.destroyWindow("Image")
    if len(points_x) == 0:
        return img
    
    points = []
    for i in range (len(points_x)):
        temp = [points_x[i], points_y[i]]
        points.append(temp)



    mask_poly = np.zeros(img.shape[:2], dtype=np.uint8)
    #bg_poly = np.zeros(img.shape[:2], dtype=np.uint8)
    points = np.asarray(points)

    cv2.fillPoly(mask_poly, [points], 255)

    obj = cv2.bitwise_and(img, img, mask=mask_poly)
    
    return obj