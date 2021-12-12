import pytube
import os
import re

if not os.path.isdir('download'):
    os.mkdir('download')

url = input('paste URL here:')
youtube = pytube.YouTube(url)
audio = youtube.streams.filter(progressive=False).get_audio_only(subtype='webm')
videos = youtube.streams.filter(progressive=False)
print('this quality was founded:')
for video in videos:
    if video.resolution is not None:
        print(f'res: {video.resolution}, itag = {video.itag}')
video = videos.get_by_itag(input('input itag to choose resolution:'))

title = video.title.replace(' ', '_')
regex = re.compile('[^\w_\@(){}\[\]]')
title = regex.sub('', title)

# 1080p mp4 - 137
video.download(filename='video.mp4')
audio.download(filename='audio.webm')


cmd = f'ffmpeg -i video.mp4 -i audio.webm -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 download/{title}.mp4'
os.system(cmd)
os.remove('audio.webm')
os.remove('video.mp4')
print(f'file "{title}.mp4" was downloaded to folder "downloads"')
