import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import json

import os

class Visualize:
    def __init__(self, root):
        self.root = root
        self.root.title("Pas de website aan")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        self.standard_text = ('Arial', 12)
        self.create_widgets()

    def create_widgets(self):
        # Create the main frame for the entire window
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the left vertical banner/frame
        self.banner = tk.Frame(main_frame, bg="lightgray", width=100)  # Width of the banner
        self.banner.pack(side=tk.LEFT, fill=tk.Y)  # Pack it on the left, fill vertically

        # Add button to the left vertical banner/frame
        self.button = tk.Button(self.banner, text="Open File", command=self.open_file, font=self.standard_text)
        self.button.pack(pady=20)  # You can adjust the padding here

        # Create the label in the main frame
        self.label = tk.Label(main_frame, text="Visualize", font=self.standard_text)
        self.label.pack(pady=20)

        # horizontal banner on the bottom of the screen
        self.banner_bottom = tk.Frame(main_frame, bg="lightgray", height=50)
        self.banner_bottom.pack(side=tk.BOTTOM, fill=tk.X)

    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            self.label.config(text=file)
        else:
            messagebox.showwarning("Warning", "No file selected")

    # Set the icon for the program
    def read_icon(self):
        try:
            # Get the absolute path to the directory containing the script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Open the _config.yml and get the icon path
            with open(os.path.join(script_dir, "_config.yml"), "r") as f:
                config_data = f.read()
                icon_name = '.'.join(config_data.split("favicon: ")[1].split('.')[:1]) + ".png"
                icon_path = os.path.join(script_dir, icon_name)[1:]
            
            print(f"Icon path: {icon_path}")
            
            # Check if the file exists
            if os.path.exists(icon_path):
                # Set the window icon for the application
                icon = Image.open(icon_path)
                icon = ImageTk.PhotoImage(icon)
                self.root.iconphoto(False, icon)
            else:
                messagebox.showwarning("Warning", f"Icon file '{icon_path}' not found. Is it a .png file?")
        except Exception as e:
            messagebox.showwarning("Warning", f"Error loading icon: {e}")


    def read_header(self):
        try:
            # Get the absolute path to the directory containing the script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Open the _config.yml and get the icon path
            with open(os.path.join(script_dir, "_data/items.json"), "r") as f:
                header_data = json.load(f)
                print(header_data)
                # add to sidebar
                item_frame = tk.Frame(self.banner, bg="lightgray", width=100, height=50)
                item_frame.pack(side=tk.TOP, fill=tk.X)
                for item in header_data:
                    item_name = item['name']
                    item_link = item['ref']
                    print(f"Item name: {item_name}, Item link: {item_link}")
                    # interactive block that can be dragged and rearranged
                    item_label = tk.Label(item_frame, text=item_name, font=self.standard_text)
                    item_label.pack(side=tk.TOP, fill=tk.X)
                    # make it draggable
                    item_label.bind("<Button-1>", self.on_drag_start)
                    item_label.bind("<B1-Motion>", self.on_drag_motion)
                    item_label.bind("<ButtonRelease-1>", self.on_drag_end)


        except Exception as e:
            messagebox.showwarning("Warning", f"Error loading header: {e}")

    def on_drag_start(self, event):
        widget = event.widget
        widget._drag_data = {'x': event.x, 'y': event.y}
        widget._drag_data["item"] = widget

    def on_drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_data['x'] + event.x
        y = widget.winfo_y() - widget._drag_data['y'] + event.y
        widget.place(x=x, y=y)

    def on_drag_end(self, event):
        widget = event.widget
        widget._drag_data = {}
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Visualize(root)
    app.read_icon()
    app.read_header()
    root.mainloop()