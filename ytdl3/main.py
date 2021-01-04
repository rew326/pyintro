from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import download_func

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
        pos_hint: {'center_x': 1.0, 'center_y': 0.2}
"""


class Main(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_string(kv)

    def download(self):
        try:
            download_func.download_func(self.root.in_class.text)
            label = self.root.ids.show
            label.text = "Success"
        except Exception as e:
            label = self.root.ids.show
            label.text = "Fail: " + str(e)

        """
        if self.root.in_class.text == 'root':
            label = self.root.ids.show
            label.text = "Sucess"
        else:
            label = self.root.ids.show
            label.text = "Fail"
        """


Main().run()
