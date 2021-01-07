from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
import helper

kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'YouTube Downloader'
        font_style: 'H3'
        pos_hint: {'center_x': 0.75, 'center_y': 0.8}
    MDTextField:
        id: text
        hint_text: 'YouTube video URL'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
        icon_right: "arrow-down-bold"
        required: True

    MDRectangleFlatButton:
        text: 'Download'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.download()

    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 0.85, 'center_y': 0.2}
"""


class Main(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        return Builder.load_string(kv)

    def download(self):
        try:
            label = self.root.ids.show
            label.text = helper.download_video(self.root.in_class.text)
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


Main().run()
