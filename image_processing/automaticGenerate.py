import cv2 
import numpy as np
import os
import random
from rembg import remove
from image_processing.update_render_cv2 import get_updated_render_cv2



def gen_image(background_image, dir_path, remove_bg= False):
    print("Generate Images Automatically")
    img_render = cv2.imread(background_image)
    dir_list = os.listdir(dir_path)
    img_bg_width = img_render.shape[1]
    img_bg_height = img_render.shape[0]
    
    for dir_name in dir_list:
        img_path = dir_path + dir_name + "/0.jpg"
        
        obj = cv2.imread(img_path)
        obj_w = (obj.shape[1])
        obj_h = (obj.shape[0])

    # downsizing objects if obj width or height is greater than base image (basic check, can be improved)
        if obj_h > img_bg_height or obj_w > img_bg_width:
            obj_w = int(obj.shape[1]/4)
            obj_h = int(obj.shape[0]/4)
            obj = cv2.resize(obj,(obj_h,obj_w))
    
    #remove background automatically
        if remove_bg == True:
            obj= remove(obj)

    ## get previous object width and location and do some random calculation so that they dont overlap

        x_offset = abs(random.randint(0, int(img_bg_width / 2)) )   #some random number (75 working good)
        y_offset = abs(random.randint(0, int(img_bg_height / 2))  )  #some random number (75 working good)
        rotation = random.randint(0,360)
        scale = random.randint(50, 100)
        print("Obj path :", img_path)
        print ("Object width :", str(obj_w))
        print("object Height : ", str(obj_h))
        print("Scale : ", str(scale))
        print("Rotation : ", str(rotation))
        print("X Offset : ", str(x_offset))
        print("y Offset :", str(y_offset))

        img_render = get_updated_render_cv2(img_render, obj, x_offset, y_offset, rotation, scale)
    
    img_write_path = "images/render/render.jpg"
    print(img_write_path)
    cv2.imwrite(img_write_path, img_render)
    cv2.imshow("test obj", img_render)
    cv2.waitKey(0)


