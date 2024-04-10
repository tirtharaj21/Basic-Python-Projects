from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_vdio(url,save_path):
    try:
        yt=YouTube(url)
        streams =yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_streams=streams.get_highest_resolution()
        highest_res_streams.download(output_path=save_path)
        print("Video downloaded successfully")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder= filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder
if __name__=="__main__": 
    root= tk.Tk()
    root.withdraw()

    video_url =input("Please enter a YouTube video url: ")
    save_dir= open_file_dialog()
    if save_dir:
        print("started download...")
        download_vdio(video_url, save_dir)
    else:
        print("Invalid saved location")