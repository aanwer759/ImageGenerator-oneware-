import PIL 
import os
import cv2
import PIL.Image 




def render_image(image_parameters):
    print ("inside render image function")

def save_image(img, image_path):
    print("save image")
    cv2.imsave(img, image_path)
    #return True

def transform_image(image, param):
    print ("transform image")

def load_image(image_path, remove_background): 
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if remove_background == True:
        print("remove background")
    return img

def add_image(background_image, foreground_image):
    #bg_w, bg_h = background_image.shape
    final_img = cv2.add(background_image, foreground_image) 
    #final_image = PIL.Image.merge(background_image.load(), foreground_image.load())
    return final_img

def convert_images_to_png(files):
    for file in files:
        img = PIL.Image.open(file)
        file_name = file.split(".")
        file_name = file_name[0] + ".png"
        img.save(file_name, "png")

# paths
background_image_path = "images/background/0.png"
forground_image_path = "images/objects/obj1/sample1.png"
image_write_path = "images/render/result1.png"
paths_list = ["images/background/0.jpg", "images/objects/obj1/sample1.jpg", "images/render/result.jpg"]
convert_images_to_png(paths_list)

bg = load_image(background_image_path, False)
fg1 = load_image(forground_image_path, False)
print(bg.shape)
print(fg1.shape)
#res = add_image(bg, fg1)

#isSaved = save_image(res, image_write_path)