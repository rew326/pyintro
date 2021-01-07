from pytube import YouTube

# Task 1.: Accept user input for video url
videoUrl = input("Video URL: ")

# Task 2.: Create a YouTube video object
video = YouTube(videoUrl)

# Task 3.: Print the title of the video
print(video.title)

# Task 4.: Download the video
video.streams.first().download()
print("Video:",video.title,"downloaded")
