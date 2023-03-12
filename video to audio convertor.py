import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
import os

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Ask user to select a video file using a file dialog box
video_path = filedialog.askopenfilename(title="Select a video file")

# Check if the user selected a file
if not video_path:
    print("No file selected. Please try again.")
    exit()

# Create a VideoFileClip object from the video file
video_clip = mp.VideoFileClip(video_path)

# Extract the audio from the video clip
audio_clip = video_clip.audio

# Create a filename for the output audio file based on the video file name
audio_filename = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"

# Write the audio to a file with the same name as the video file
audio_clip.write_audiofile(audio_filename)

# Close the video and audio clips
video_clip.close()
audio_clip.close()

print("Audio extracted and saved as: " + audio_filename)



#pip install moviepy
#pip install pydub
