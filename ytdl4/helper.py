from pytube import Playlist
import pytube


def load_playlist(url):

    playlist = Playlist(url)

    return playlist, 0


# Task 1.: Define a "download_func" function which downloads a video given
# given 2 arguments: list of urls in a playlist and a position of a video in playlist
def download_video(playlist, vidIndex):
    urlParsed = playlist[vidIndex]

    youtube = pytube.YouTube(urlParsed)
    video = youtube.streams.first()
    video.download('./videos/')
