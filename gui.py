import cv2
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

def load_image():
    """Load an image file and display it in the GUI."""
    global img_label, img

    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
    if not file_path:
        return  # No file selected

    # Load the image using OpenCV
    cv_img = cv2.imread(file_path)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Tkinter

    # Convert OpenCV image to PIL Image
    img = Image.fromarray(cv_img)

    # Convert PIL Image to ImageTk PhotoImage
    img_tk = ImageTk.PhotoImage(img)

    # Display the image in the Label widget
    img_label.config(image=img_tk)
    img_label.image = img_tk

# Initialize Tkinter window
root = Tk()
root.title("Image Viewer")

# Create a Label widget to display the image
img_label = Label(root)
img_label.pack()

# Create a button to load an image
load_button = Button(root, text="Load Image", command=load_image)
load_button.pack()

# Run the Tkinter event loop
root.mainloop()