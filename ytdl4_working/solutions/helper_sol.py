from pytube import Playlist
from pytube import YouTube
import pytube

# Task 1.: Define a "load_playlist" function which accepts 1 parameter:
# - url - a url of a playlist
# and returns:
# - the pytube Playlist object
# - list of YouTube object (video) for each item in the Playlist object
def load_playlist(url):
    playlist = Playlist(url)
    ytvideos = []
    ytvideotitles = []

    for link in playlist:
        ytvideo = YouTube(link)
        ytvideos.append(ytvideo)

    return playlist, ytvideos

# Task 2.: Define a "download_video" function which downloads a video and accepts 2 parameters:
# - index - a current int index in a playlist
# - playlist - a list of urls in a playlist
# and returns a successful download message
def download_video(index, playlist):

    url = playlist[index]

    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download('./videos/')

    return "Video successfully downloaded"

# Task 3.: Define a "next_video" function which accepts 2 parameters:
# - index - a current int index in a playlist
# - playlist - a list of urls in a playlist
# and returns the next index or the first index if we are at the end of the playlist
def next_video(index, playlist):
    if index + 1 == len(playlist):
        return 0
    else:
        return index + 1
