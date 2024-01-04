import os
import tkinter as tk


#add path to location: ex. "C:/Users/tirth/Downloads/"
path = "C:/Users/tirth/Downloads/"

#add personalized filenames here as strings. Don't forget extension(.pdf, .txt, etc.)
presetFiles = ["TirthResume.pdf", "TirthResumeI.pdf", "TirthResumeF.pdf"]


#delete file function. $preset_file will be used for presets
def deleteFile(preset_file=None):
    
    #destroys existing message
    if hasattr(deleteFile, 'message'):
      deleteFile.message.destroy()
      
    #checks if userinput name or preset
    if preset_file is None:
        file = entry1.get()
    else:
        file = preset_file
    
    file_path = path + file
    
    #remove file
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
title = tk.Label(root, text="Remove File From", font=("Ariel", 15, "bold"))
title.pack(padx=20, pady=(15,0))
title2 = tk.Label(root, text=path, font=("Ariel", 10, "italic"))
title2.pack(pady=2)

#entry field 
entry1_label = tk.Label(root, text="Enter File Name", font=("Ariel", 12, "bold")) 
entry1_label.pack(pady=(10, 5))

entry1 = tk.Entry(root) 
entry1.pack(pady=(0, 10))

button1 = tk.Button(text='Delete', command=deleteFile)
button1.pack(pady=(5, 15))

#presets 
presetTitle = tk.Label(root, text="Presets", font=("Ariel", 12, "bold"))
presetTitle.pack(pady=10)

for pf in presetFiles:
    button2 = tk.Button(text=pf, command=lambda file_name=pf: deleteFile(file_name))
    button2.pack(pady=5)


root.mainloop()

    