from UI.gui import App
from image_processing.automaticGenerate import gen_image
import cv2
from rembg import remove
if __name__ == "__main__":

    # automatic generation
    gen_image("images/background/0.jpg", "images/objects/", True)
    #img = cv2.imread("images/objects/obj1/0.jpg")
    #print(img.size)
    #img_bg = remove(img)
    #cv2.imshow("test image", img_bg)
    #cv2.waitKey(0)
    # Create and run the Tkinter app
    #app = App()
    #app.run()