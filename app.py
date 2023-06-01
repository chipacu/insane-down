from tkinter import*
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

def select_path():
    path = filedialog.askdirectory()
    pathlabel.config(text=path)

def download():
    get_link = entry.get()
    user_path = pathlabel.cget("text")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    shutil.move(mp4_video, user_path)
    alert.config(text="All done!")

root = Tk()
root.config(bd=15)
root.title("Insane Video Downloader")

label = Label(root, text="Paste the URL here: ")
label.pack()

entry = Entry(root, width=48)
entry.pack()

pathlabel = Label(root, text="...")
pathlabel.pack()

destbtn = Button(root, text="Select path", command=select_path)
destbtn.pack()

downloadbtn = Button(root, text="Download", command=download)
downloadbtn.pack(pady=10)

alert = Label(root, text="")
alert.pack()

root.mainloop()