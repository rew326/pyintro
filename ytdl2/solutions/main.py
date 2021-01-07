from pytube import Playlist
from pytube import YouTube

# Task 1.: Accept user input for playlist url
# Get a playlist
playlistUrl = input("Playlist URL: ")

# Task 2.: Print number of videos in a playlist
playlist = Playlist(playlistUrl)
no_vids = len(playlist)
print("The playlist has", no_vids, "videos")

# Task 3.: Print the title of each url
for url in playlist:
    video = YouTube(url)
    print(video.title)

# Task 4.: Download all videos
for url in playlist:
    video = YouTube(url)
    video.streams.first().download()
    print("Video:",video.title,"downloaded")
