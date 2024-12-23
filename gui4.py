import cv2
from tkinter import Tk, Label, Button, filedialog, Toplevel, Scale
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from image_manipulation import open_image_window

import tkinter as tk

class TkinterApp:
    def __init__(self, title="Tkinter App", width=400, height=300):
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
        
        # Create a Label widget
        self.label = tk.Label(self.window, textvariable=self.label_text)
        self.label.pack(pady=20)
        
        # Create a Button widget to change the label text
        self.change_text_button = tk.Button(self.window, text="Change Text", command=self.change_text)
        self.change_text_button.pack(pady=10)
        
        # Create a Scale widget to control label font size
        self.font_scale = tk.Scale(self.window, from_=8, to_=48, orient=tk.HORIZONTAL, label="Font Size", command=self.change_font_size)
        self.font_scale.set(16)  # Set initial font size
        self.font_scale.pack(pady=10)
        
        # Create an Entry widget to accept user input
        self.entry = tk.Entry(self.window)
        self.entry.pack(pady=10)
        
        # Create a Button widget to display entry text
        self.display_entry_button = tk.Button(self.window, text="Display Entry", command=self.display_entry)
        self.display_entry_button.pack(pady=10)

    def change_text(self):
        """Change the label text when the button is clicked."""
        self.label_text.set("Text Changed!")

    def change_font_size(self, value):
        """Change the font size of the label when the scale value changes."""
        font_size = int(value)
        self.label.config(font=("Arial", font_size))

    def display_entry(self):
        """Display the text entered in the Entry widget."""
        entered_text = self.entry.get()
        self.label_text.set(f"Entered Text: {entered_text}")

    def run(self):
        """Run the Tkinter event loop."""
        self.window.mainloop()

# Example usage
if __name__ == "__main__":
    # Create and run the Tkinter app
    app = TkinterApp(title="My First Tkinter App")
    app.run()