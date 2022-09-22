import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("500x300")

image = Image.open("bfbanner.png").resize((400, 200))
photo = ImageTk.PhotoImage(image)

label1 = ttk.Label(root, text="He's no good to me dead", image=photo, compound="top")
label1.pack()

root.mainloop()