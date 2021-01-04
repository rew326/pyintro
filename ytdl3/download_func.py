import pytube

def download_func(url):
    urlParsed = url

    youtube = pytube.YouTube(urlParsed)
    video = youtube.streams.first()
    video.download()
