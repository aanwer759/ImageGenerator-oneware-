import cv2
from tkinter import Tk, Label, Button, filedialog, Toplevel, Scale
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from image_manipulation import open_image_window


root = Tk()
root.title("Main Window")
img = Image.open("images/background/0.jpg")
img_tk = ImageTk.PhotoImage(img)

# Create a label in the new window to display the image
img_label = Label(root, image=img_tk)
img_label.image = img_tk  # Keep a reference to avoid garbage collection
img_label.pack()
# Create a button in the main window to open a new image viewer window
open_button = Button(root, text="Add object", command=lambda: open_image_window(root))
open_button.pack()

# Run the Tkinter event loop
root.mainloop()