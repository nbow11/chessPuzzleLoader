
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

root = tk.Tk()

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to the image to prevent garbage collection
        save_button.config(state=tk.NORMAL)

def save_image():
    image = image_label.image
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if file_path:
        image.write(file_path)

open_button = tk.Button(root, text="Open image", command=open_image)
open_button.pack()

image_label = tk.Label(root)
image_label.pack()

save_button = tk.Button(root, text="Confirm", command=save_image, state=tk.DISABLED)
save_button.pack()

root.mainloop()
