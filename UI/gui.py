import cv2
from tkinter import Tk, Label, Button, filedialog, Toplevel, Scale
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#
from image_processing.create_mask_cv2 import process_image
from image_processing.pick_location_cv2 import pick_location_imp
from image_processing.update_render_cv2 import get_updated_render_cv2
import tkinter as tk
import random

class App:
    def __init__(self, title="Image Generator", width=1024, height=786):

        """Initialize the Tkinter application."""
        self.window = tk.Tk()  # Create the main window
        self.window.title(title)  # Set window title
        self.window.geometry(f"{width}x{height}")  # Set window size
        
        # defualt values 
        self.rotate = 0
        self.scale = 100
        self.locx = 50
        self.locy = 50
        
        # Call to setup widgets
        self.setup_widgets()

    def setup_widgets(self):
        """Setup widgets for the Tkinter application."""
    
        #lable 
        self.label_text = tk.StringVar(value="Background")
        self.label = tk.Label(self.window, textvariable= self.label_text)
        self.label.pack(pady=5)

        ## add image widget
        self.bgimg_path = "images/background/0.jpg"
        self.img = Image.open(self.bgimg_path)
        self.img_tk = ImageTk.PhotoImage(self.img)

# Create a label in the new window to display the image
        self.img_label = Label(self.window, image=self.img_tk)
        self.img_label.image = self.img_tk  # Keep a reference to avoid garbage collection
        self.img_label.pack(pady=5)

        # Create a Button widget to Add Image
        self.add_image_button = tk.Button(self.window, text="Add Image", command=self.add_object)
        self.add_image_button.pack(pady=5)

        # Create a Button widget to Save Image
        self.add_image_button = tk.Button(self.window, text="Save Image", command=self.save_image)
        self.add_image_button.pack(pady=5)
        #lable 
        self.label_text = tk.StringVar(value="Preview")
        self.label = tk.Label(self.window, textvariable= self.label_text)
        self.label.pack(pady=20)
        ## create preview label
        self.img_render = self.img
        self.img_tk_render = ImageTk.PhotoImage(self.img_render)
        self.img_label_render = Label(self.window, image=self.img_tk_render)
        self.img_label_render.image = self.img_tk_render  # Keep a reference to avoid garbage collection
        self.img_label_render.pack(pady=5)

    def add_object(self):
        print("add object")
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
        if not self.file_path:
            return  # Exit if no file is selected

    # Create a new top-level window
        self.new_window = Toplevel(self.window)
        self.new_window.title("Image Viewer")
        self.new_window.geometry("512x512")

    # Load the image using OpenCV
        #self.cv_imgobj = cv2.imread(self.file_path)
    #cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Tkinter
        self.extract_image = process_image(self.file_path, self.bgimg_path)
        self.extract_image = cv2.cvtColor(self.extract_image, cv2.COLOR_BGR2RGB)
        
    # Convert OpenCV image to PIL Image
        self.imgobj = Image.fromarray(self.extract_image)
        # Convert PIL Image to ImageTk PhotoImage
        self.img_tk_obj = ImageTk.PhotoImage(self.imgobj)
        self.img_labelobj = Label(self.new_window, image=self.img_tk_obj)
        self.img_labelobj.image = self.img_tk_obj  # Keep a reference to avoid garbage collection
        self.img_labelobj.pack(pady=10)
        #Rotation lable 
        self.label_text = tk.StringVar(value="Rotation Angle")
        self.label = tk.Label(self.new_window, textvariable= self.label_text)
        self.label.pack(pady=5)
        #Rotation slider 
        self.current_rot_value= DoubleVar()
        self.rot_slider = Scale(self.new_window, from_=0, to=360, orient='horizontal', variable=self.current_rot_value, command = self.on_rot_value_change)
        self.rot_slider.pack(pady=5)
        #scale lable 
        self.label_text = tk.StringVar(value="Scale Percentage")
        self.label = tk.Label(self.new_window, textvariable= self.label_text)
        self.label.pack(pady=10)
        ## scale Slider 
        self.current_scale_value = DoubleVar()
        self.current_scale_value.set(100)
        self.scale_slider = Scale(self.new_window, from_=0, to=250, orient='horizontal', variable=self.current_scale_value, command = self.on_scale_value_change)
        self.scale_slider.pack(pady=10)
        #pick location button 
        pick_location_button = Button(self.new_window, text = "Pick Location", command = self.pick_location)
        pick_location_button.pack()
        close_button = Button(self.new_window, text = "Add", command = self.update_render) 
        close_button.pack(pady=10)
    
    def on_rot_value_change(self, value):
        print("Rotation value : ", str(value))
        self.rotate = value
    
    def on_scale_value_change(self, value):
        print("Scale Value : ", str(value))
        self.scale = value

    def pick_location(self):
        self.locx , self.locy = pick_location_imp(self.bgimg_path)
        print(self.locx, self.locy)
        
        
        
    def update_render(self):
        
        self.img_render = get_updated_render_cv2(self.img_render, self.extract_image, self.locx, self.locy, self.rotate, self.scale) 
        print("update preview")
          
        self.img_render = Image.fromarray(self.img_render)
        self.img_tk_render = ImageTk.PhotoImage(self.img_render)
        self.img_label_render.destroy()
        self.img_label_render = Label(self.window, image=self.img_tk_render)
        self.img_label_render.image = self.img_tk_render  # Keep a reference to avoid garbage collection
        self.img_label_render.pack(pady=5)
        ## setting random x and y positions for next image if position is not selected
        self.locx = random.randint(1, 100)
        self.locy = random.randint(1, 100)
        #self.img_labelobj.destroy()
        self.new_window.destroy()
        
    def save_image(self):
        print("Save image")
        self.save_file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("All files", "*.*")])
        print("save file path :", self.save_file_path)
        self.img_render.save(self.save_file_path)

    def run(self):
        
        self.window.mainloop()

