# -----------------------------------------------
# Simple Text Editor App (Tkinter GUI)
# Created by: Subarna Ghosh
# -----------------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Simple Text Editor - Subarna Ghosh")
root.geometry("800x600")

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12))
text.pack(expand=True, fill=tk.BOTH)

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully!")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
