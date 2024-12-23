import cv2
from tkinter import Tk, Label, Button, filedialog, Toplevel, Scale
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#from image_manipulation import open_image_window
from create_mask import process_image
from pick_location_cv2 import pick_location_imp
from update_render_cv2 import get_updated_render_cv2
import tkinter as tk

class TkinterApp:
    def __init__(self, title="Tkinter App", width=1024, height=786):
        """Initialize the Tkinter application."""
        self.window = tk.Tk()  # Create the main window
        self.window.title(title)  # Set window title
        self.window.geometry(f"{width}x{height}")  # Set window size
        
        # Example variables for demonstration
        self.label_text = tk.StringVar(value="Hello, Tkinter!")
        
        # Call to setup widgets
        self.setup_widgets()

    def setup_widgets(self):
        """Setup widgets for the Tkinter application."""
        
        ## add image widget
        self.bgimg_path = "images/background/0.jpg"
        self.img = Image.open(self.bgimg_path)
        self.img_tk = ImageTk.PhotoImage(self.img)

# Create a label in the new window to display the image
        self.img_label = Label(self.window, image=self.img_tk)
        self.img_label.image = self.img_tk  # Keep a reference to avoid garbage collection
        self.img_label.pack()

        # Create a Button widget to change the label text
        self.change_text_button = tk.Button(self.window, text="Add Image", command=self.add_object)
        self.change_text_button.pack(pady=10)

        ## create preview label
        self.img_render = self.img
        self.img_tk_render = ImageTk.PhotoImage(self.img_render)
        self.img_label_render = Label(self.window, image=self.img_tk_render)
        self.img_label_render.image = self.img_tk_render  # Keep a reference to avoid garbage collection
        self.img_label_render.pack()
        
    def add_object(self):
        print("add object")
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
        if not self.file_path:
            return  # Exit if no file is selected

    # Create a new top-level window
        self.new_window = Toplevel(self.window)
        self.new_window.title("Image Viewer")

    # Load the image using OpenCV
        self.cv_imgobj = cv2.imread(self.file_path)
    #cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Tkinter
        self.extract_image = process_image(self.cv_imgobj)
        self.extract_image = cv2.cvtColor(self.extract_image, cv2.COLOR_BGR2RGB)
    
    # Convert OpenCV image to PIL Image
        self.imgobj = Image.fromarray(self.extract_image)
        # Convert PIL Image to ImageTk PhotoImage
        self.img_tk_obj = ImageTk.PhotoImage(self.imgobj)
        self.img_labelobj = Label(self.new_window, image=self.img_tk_obj)
        self.img_labelobj.image = self.img_tk_obj  # Keep a reference to avoid garbage collection
        self.img_labelobj.pack()
        #lable 
        self.label_text = tk.StringVar(value="Rotation")
        self.label = tk.Label(self.new_window, textvariable= self.label_text)
        self.label.pack(pady=20)
        self.current_value= DoubleVar()
        self.slider = Scale(self.new_window, from_=0, to=100, orient='horizontal', variable=self.current_value, command = self.on_value_change)
        self.slider.pack()
        pick_location_button = Button(self.new_window, text = "Pick Location", command = self.pick_location)
        pick_location_button.pack()
        close_button = Button(self.new_window, text = "Add", command = self.update_render) 
        close_button.pack()
    
    def on_value_change(self, value):
        self.imgobj.rotate(int(value))
        print("value : ", value)
        self.rotate = value
    

    def pick_location(self):
        self.locx , self.locy = pick_location_imp(self.bgimg_path)
        
        
        
    def update_render(self):
        self.rotate = 0
        self.updated_preview = get_updated_render_cv2(self.img_render, self.extract_image, self.locx, self.locy, self.rotate) 
        print("update preview")
        self.updated_preview = Image.fromarray(self.updated_preview)
        self.img_render = self.updated_preview
        self.img_tk_render = ImageTk.PhotoImage(self.img_render)
        self.img_label_render.destroy()
        self.img_label_render = Label(self.window, image=self.img_tk_render)
        self.img_label_render.image = self.img_tk_render  # Keep a reference to avoid garbage collection
        self.img_label_render.pack()
        self.new_window.destroy()
        

    def run(self):
        """Run the Tkinter event loop."""
        self.window.mainloop()

# Example usage
if __name__ == "__main__":
    # Create and run the Tkinter app
    app = TkinterApp(title="Image Generator")
    app.run()