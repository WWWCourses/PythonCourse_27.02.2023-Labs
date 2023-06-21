from pytube import YouTube
from pytube.cli import on_progress

url = 'https://youtu.be/aY1uFx4kTIw?list=PLHr3FWbW-hj6s13V_lFbwR6_V6PFDiBW4'

video = YouTube(url, on_progress_callback=on_progress)

stream = video.streams.get_lowest_resolution()

stream.download()

print('Download complete')