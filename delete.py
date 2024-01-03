import os
import tkinter as tk

path = "C:/Users/tirth/Downloads/xd.txt"

#create window 
root = tk.Tk()
root.geometry("500x500")
root.title("File Remover")

#title
title = tk.Label(root, text="Remove File From Dowloads folder", font=("Ariel", 15, "bold"))
title.pack(padx=20, pady=20)

#entry field
entry1_label = tk.Label(root, text="Enter File Name", font=("Ariel", 12)) 
entry1_label.pack(pady=5)

entry1_label = tk.Entry(root) 
entry1_label.pack(pady=0)



root.mainloop()

try: 
    os.remove(path)
except FileNotFoundError:
    print("file not found")
    