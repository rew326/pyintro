from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from pytube import Playlist
from pytube import YouTube
import pytube
import requests
import helper

kv = """
ScreenManager:
    in_class: in_class

    MenuScreen:
        name: 'menu'
        MDLabel:
            text: 'YouTube Downloader'
            font_style: 'H3'
            pos_hint: {'center_x': 0.75, 'center_y': 0.8}
        MDTextField:
            id: in_class
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
                vidthumbnail.source = root.images[root.currVid]
                viddownload.text = "Download: " + str(root.ytvidtitles[root.currVid])
                root.current = 'thumbnail'

    VideoScreen:
        name: 'thumbnail'
        id: vidscreen
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
                vidthumbnail.source = root.images[root.currVid]
                viddownload.text = "Download: " + str(root.ytvidtitles[root.currVid])
        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: root.current = 'menu'
        MDLabel:
            text: ''
            id: show
            pos_hint: {'center_x': 0.9, 'center_y': 0.7}

"""


class MenuScreen(Screen):
    pass

class VideoScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(VideoScreen(name='thumbnail'))

class Main(MDApp):

    in_class = ObjectProperty(None)
    ytvids = None
    ytvidtitles = None
    images = None
    playlist = None
    currVid = None

    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        screen = Builder.load_string(kv)
        return screen

    def load(self):
        self.root.currVid = 0
        self.root.playlist, self.root.ytvids = helper.load_playlist(self.root.in_class.text)
        self.root.ytvidtitles = []
        self.root.images = []

        for i in range(len(self.root.ytvids)):

            ytvid = self.root.ytvids[i]

            img_data = requests.get(ytvid.thumbnail_url).content
            with open("images/{}.jpg".format(i), 'wb') as handler:
                handler.write(img_data)

            self.root.ytvidtitles.append(ytvid.title)
            self.root.images.append('images/image' + str(i) + '.jpg')

    # Shift currVid index by one
    def nextVid(self):
        self.root.currVid = helper.next_video(self.root.currVid, self.root.playlist)
        label = self.root.ids.show
        label.text = ""

    # Download function
    def downloadVid(self):
        try:
            label = self.root.ids.show
            label.text = helper.download_video(self.root.currVid, self.root.playlist)
        except Exception as e:
            label = self.root.ids.show
            label.text = "Fail: " + str(e)

    # Show text popup box on exit
    def on_request_close(self, *args):
        self.textpopup(title='Exit', text='Are you sure?')
        return True

    # Exit text popup box
    def textpopup(self, title='', text=''):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        mybutton = Button(text='OK', size_hint=(1, 0.25))
        box.add_widget(mybutton)
        popup = Popup(title=title, content=box, size_hint=(None, None), size=(600, 300))
        mybutton.bind(on_release=self.stop)
        popup.open()

# Run application
Main().run()
