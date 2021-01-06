from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from pytube import Playlist
from pytube import YouTube
import pytube
import requests

kv = """
ScreenManager:
    MenuScreen:
    VideoScreen:
<MenuScreen>:
    name: 'menu'
    in_class: text
    MDLabel:
        text: 'YouTube Downloader'
        font_style: 'H3'
        pos_hint: {'center_x': 0.75, 'center_y': 0.8}
    MDTextField:
        id: text
        hint_text: 'YouTube playlist URL'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
        icon_right: "arrow-down-bold"
        required: True

    MDRectangleFlatButton:
        text: 'Load'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.load()
            root.manager.current = 'thumbnail'

    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 1.0, 'center_y': 0.2}

<VideoScreen>:
    name: 'thumbnail'
    Image:
        id: vidthumbnail
        source: ''
        keep_ratio: False
        allow_stretch: False
        opacity: 0.9
        size_hint: 0.4, 0.3
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        border: (10,10,10,10)
    MDRectangleFlatButton:
        id: viddownload
        text: 'Click "Next"'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.downloadVid()
    MDRectangleFlatButton:
        text: 'Next'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            app.nextVid()
            root.changeText()
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""


class MenuScreen(Screen):
    pass

class VideoScreen(Screen):

    def __init__(self,**kwargs):
        super(VideoScreen,self).__init__(**kwargs)

    def changeText(self):
        global playlist
        global currVid

        ytvid = YouTube(playlist[currVid])
        img_data = requests.get(ytvid.thumbnail_url).content
        with open("images/image_name_{}.jpg".format(currVid), 'wb') as handler:
            handler.write(img_data)
        self.ids.vidthumbnail.source = "images/image_name_{}.jpg".format(currVid)
        self.ids.viddownload.text = "Download: " + ytvid.title

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(VideoScreen(name='thumbnail'))


class Main(MDApp):

    in_class = ObjectProperty(None)

    playlist = None
    currVid = None

    def build(self):
        screen = Builder.load_string(kv)
        return screen

    def load(self):
        global playlist
        global currVid

        playlist = Playlist('https://www.youtube.com/playlist?list=PLg1MZ2KOzNJxdrmSXv0fQ9a5vuyfWtdKv')
        currVid = -1
        sm.current = 'thumbnail'
        self.nextVid()

    def nextVid(self):
        global playlist
        global currVid

        if currVid + 1 == len(playlist):
            currVid = 0
        else:
            currVid += 1

    def downloadVid(self):
        global playlist
        global currVid

        url = playlist[currVid]

        youtube = pytube.YouTube(url)
        video = youtube.streams.first()

        video.download()


Main().run()
