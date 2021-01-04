import pytube

url = 'https://www.youtube.com/watch?v=mFCKLBsmF_w'

youtube = pytube.YouTube(url)
video = youtube.streams.first()

video.download('')
