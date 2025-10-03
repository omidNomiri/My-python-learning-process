from moviepy import editor
from time import time

start_time = time()

for i in range(1 ,4):
	video = editor.VideoFileClip(f"Assignment_24\input\music_{str(i)}.mp4")
	output = f"music_{str(i)}.mp3"
	video.audio.write_audiofile(str(output))

end_time = time()
print(end_time - start_time)
