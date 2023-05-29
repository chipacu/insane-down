from tkinter import*
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

root = Tk()
root.title("Insane Video Downloader")

label = Label(root, text="Paste the URL here: ")
label.pack()

entry = Entry(root, width=48)
entry.pack()

destbtn = Button(root, text="Select path")
destbtn.pack()

downloadbtn = Button(root, text="Download")
downloadbtn.pack(pady=10)

alert = Label(root, text="")

root.mainloop()