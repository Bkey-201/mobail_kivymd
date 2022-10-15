from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Marina MSW,I'm Bkey-201", halign="center")


MainApp().run()