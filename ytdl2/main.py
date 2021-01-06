from pytube import Playlist
from pytube import YouTube

# Get a playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLg1MZ2KOzNJxdrmSXv0fQ9a5vuyfWtdKv')

# Find number of videos in the Playlist
no_vids = len(playlist)
print("The playlist has", no_vids, "videos")

# Print title of each playlist
'''
for url in playlist:
    video = YouTube(url)
    print(video.title)
'''

# Download all videos

for url in playlist:
    video = YouTube(url)
    video.streams.first().download()
    print("Video:",video.title,"downloaded")
