# -----------------------------------------------
# Python Image Slideshow App (Tkinter + Pillow)
# Created by: Subarna Ghosh
# -----------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Python Image Slideshow App - Subarna Ghosh")
root.geometry("900x620")

image_size = (800, 480)
photo_images = []
current_index = 0
is_playing = False

image_label = tk.Label(
    root,
    text="Click 'Select Images' to choose photos, then click 'Play Slideshow'",
    font=("Arial", 13)
)
image_label.pack(pady=20, expand=True)

def select_images():
    global photo_images, current_index, is_playing
    file_paths = filedialog.askopenfilenames(
        title="Select Images for Slideshow",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if not file_paths:
        return

    photo_images.clear()
    current_index = 0
    is_playing = False

    for path in file_paths:
        img = Image.open(path)
        img = img.resize(image_size)
        photo_images.append(ImageTk.PhotoImage(img))

    image_label.config(image=photo_images[0], text="")
    image_label.image = photo_images[0]

def show_next_slide():
    global current_index
    if not is_playing or not photo_images:
        return

    photo = photo_images[current_index]
    image_label.config(image=photo, text="")
    image_label.image = photo

    current_index = (current_index + 1) % len(photo_images)
    root.after(2000, show_next_slide)

def start_slideshow():
    global is_playing
    if not photo_images:
        messagebox.showwarning("No Images Selected", "Please click 'Select Images' first to load photos.")
        return
    if not is_playing:
        is_playing = True
        show_next_slide()

def stop_slideshow():
    global is_playing
    is_playing = False

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

select_button = tk.Button(
    button_frame,
    text="Select Images",
    font=("Arial", 12),
    command=select_images
)
select_button.pack(side=tk.LEFT, padx=10)

play_button = tk.Button(
    button_frame,
    text="Play Slideshow",
    font=("Arial", 12),
    command=start_slideshow
)
play_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(
    button_frame,
    text="Stop Slideshow",
    font=("Arial", 12),
    command=stop_slideshow
)
stop_button.pack(side=tk.LEFT, padx=10)

root.mainloop()

