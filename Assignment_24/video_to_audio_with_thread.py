from moviepy import editor
from time import time
from threading import Thread

start_time = time()
threads = []

def transformer(i):
    video = editor.VideoFileClip(f"Assignment_24\input\music_{str(i)}.mp4")
    output = f"music_{str(i)}.mp3"
    video.audio.write_audiofile(str(output))

for i in range(1 ,4):
    threads.append(Thread(target=transformer, args=[i]))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time()
print(end_time - start_time)
