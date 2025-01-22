import tkinter as tk
from abc import ABC, abstractmethod
import playsound
from playsound import playsound

# right now we will assume the file already 
def execute_audio(event):
    label = tk.Label(root,text="Great Job")
    label.pack()
    print("HELLO THERE")
    playsound("./helloeverybodyobama.mp3")
    pass

root = tk.Tk()
root.geometry("1920x1080")
button = tk.Button(root, text="Click Me", padx=50, pady=50)
button.bind('<Button>', execute_audio)
button.pack()
root.mainloop()