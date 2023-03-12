import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
import os


root = tk.Tk()

# himanshu
root.withdraw()


video_path = filedialog.askopenfilename(title="Select a video file")


if not video_path:
    print("No file selected. Please try again.")
    exit()

video_clip = mp.VideoFileClip(video_path)


audio_clip = video_clip.audio

audio_filename = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"


audio_clip.write_audiofile(audio_filename)


video_clip.close()
audio_clip.close()

print("Audio extracted and saved as: " + audio_filename)




