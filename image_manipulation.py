import cv2
from tkinter import Tk, Label, Button, filedialog, Toplevel, Scale
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from create_mask import process_image
import numpy as np


def on_value_change(value):
    print(value)


def open_image_window(root):
    """Open a new window to display the selected image."""
    
    rotation=0

    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
    if not file_path:
        return  # Exit if no file is selected

    # Create a new top-level window
    new_window = Toplevel(root)
    new_window.title("Image Viewer")

    # Load the image using OpenCV
    cv_img = cv2.imread(file_path)
    #cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Tkinter
    extract_image = process_image(cv_img)
    extract_image = cv2.cvtColor(extract_image, cv2.COLOR_BGR2RGB)
    
    # Convert OpenCV image to PIL Image
    img = Image.fromarray(extract_image)
    current_value= DoubleVar()
    slider = Scale(new_window, from_=0, to=100, orient='horizontal', variable=current_value, command = on_value_change)
    slider.pack()
    print("executed once")
   
    # Convert PIL Image to ImageTk PhotoImage
    img_tk = ImageTk.PhotoImage(img)

    # Create a label in the new window to display the image
    img_label = Label(new_window, image=img_tk)
    img_label.image = img_tk  # Keep a reference to avoid garbage collection
    img_label.pack()

    # Add a close button to the new window
    close_button = Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack()