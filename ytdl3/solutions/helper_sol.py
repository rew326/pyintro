import pytube

# Task 1.: Define a "download_video" function which downloads a video and accepts 1 parameter:
# - url - a url of a video which should be downloaded
# and returns a successful download message
def download_video(url):

    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download('./videos/')

    return "Video successfully downloaded"
