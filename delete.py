import os
import tkinter as tk

path = "C:/Users/tirth/Downloads/"

def deleteFile(preset_file=None):
    
    #destroys existing message
    if hasattr(deleteFile, 'message'):
      deleteFile.message.destroy()
      
    #checks if userinput file or preset
    if preset_file is None:
        file = entry1.get()
    else:
        file = preset_file
    
    file_path = path + file
    
    try: 
        os.remove(file_path)
        deleteFile.message = tk.Label(root, text=file + " removed", font=("Arial", 10, "bold"))
    except FileNotFoundError:
        deleteFile.message = tk.Label(root, text=file + " not found", font=("Arial", 10, "bold"))
  
    deleteFile.message.pack(padx=3, pady=3)


#create window 
root = tk.Tk()
root.geometry("500x500")
root.title("File Remover")

#title
title = tk.Label(root, text="Remove File From Dowloads", font=("Ariel", 15, "bold"))
title.pack(padx=20, pady=20)

#entry field
entry1_label = tk.Label(root, text="Enter File Name", font=("Ariel", 12)) 
entry1_label.pack(pady=5)

entry1 = tk.Entry(root) 
entry1.pack(pady=0)

button1 = tk.Button(text='Delete', command=deleteFile)
button1.pack(pady=10)
root.mainloop()

    