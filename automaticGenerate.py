import cv2 
import numpy as np
import os
import random
from image_processing.update_render_cv2 import get_updated_render_cv2



def gen_image(background_image, dir_path):
    print("Generate Images Automatically")
    img_render = cv2.imread(background_image)
    dir_list = os.listdir(dir_path)
    for dir_name in dir_list:
        img_path = dir_path + dir_name + "/0.jpg"
        print("image path :", img_path)
        obj = cv2.imread(img_path)
        obj_w = int(obj.shape[1]/4)
        obj_h = int(obj.shape[0]/4)
        obj = cv2.resize(obj,(obj_h,obj_w))
    ##todo : remove background automatically
    #obj= remove_background(obj)
    ## get previous object width and location and do some random calculation so that they dont overlap
    
        x_offset = abs(random.randint(0, obj_w * 2 )  - 75) #some random number (100 working good)
        y_offset = abs(random.randint(0, obj_h * 2) - 75 ) # some ransom number (100 working good)
        rotation = random.randint(0,360)
        scale = random.randint(25, 100)
    
        img_render = get_updated_render_cv2(img_render, obj, x_offset, y_offset, rotation, scale)
    
    img_write_path = dir_path + "render/render.jpg"
    cv2.imwrite(img_write_path, img_render)
    cv2.imshow("test obj", img_render)
    cv2.waitKey(0)


