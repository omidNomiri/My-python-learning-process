from moviepy import editor
from time import time

start_time = time()

video = editor.VideoFileClip("your mp4 file path")
output = "your output mp3 file format"
video.audio.write_audiofile(str(output))

end_time = time()
print(end_time - start_time)
