import cv2
from tkinter import Tk, Label, Button, filedialog, Toplevel
from PIL import Image, ImageTk


def select_area():
    print("create Mask")
    #call masking area ??
    

def open_image_window():
    """Open a new window to display the selected image."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
    if not file_path:
        return  # Exit if no file is selected

    # Create a new top-level window
    new_window = Toplevel(root)
    new_window.title("Image Viewer")

    # Load the image using OpenCV
    cv_img = cv2.imread(file_path)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Tkinter

    # Convert OpenCV image to PIL Image
    img = Image.fromarray(cv_img)

    # Resize image if it's too large
    max_size = (600, 600)  # Adjust window size if needed
    img.thumbnail(max_size)

    # Convert PIL Image to ImageTk PhotoImage
    img_tk = ImageTk.PhotoImage(img)

    # Create a label in the new window to display the image
    img_label = Label(new_window, image=img_tk)
    img_label.image = img_tk  # Keep a reference to avoid garbage collection
    img_label.pack()

    edit_image_button = Button(new_window, text="Select Area", command= select_area)
    # Add a close button to the new window
    close_button = Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack()

# Initialize Tkinter main window
root = Tk()
root.title("Main Window")

# Create a button in the main window to open a new image viewer window
open_button = Button(root, text="Open Image Viewer", command=open_image_window)
open_button.pack()

# Run the Tkinter event loop
root.mainloop()