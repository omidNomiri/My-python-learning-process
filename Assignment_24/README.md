# Comparison of Python script speed

## Target

The goal of this project is to compare the execution speed of two Python scripts that use the MoviePy library to extract audio from multiple MP4 files.

## script

1. "video_to_audio.py".
2. "video_to_audio_with_thread.py".

**(Please replace these locations with actual file names.)**

## Additional considerations

**Formats:**

- Specify input MP4 file formats, as they can affect processing time.

**threading:**

- One of the scripts uses threading to parallelize audio extraction.

## Result

- Without thread: 7.50431227684021 sec
- With thread: 4.791076421737671 sec

Here you can see when we use threads to make apps faster.
