from kivymd.app import MDApp
from kivy.uix.effectwidget import EffectWidget
from kivymd.uix.screenmanager import MDScreenManager
from start_screens import *

shaders=False

class RandomApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_text_color = "Custom"
        if shaders:
            self.root = EffectWidget()
        self.manager=MDScreenManager()
        if shaders:
            self.root.add_widget(self.manager)
        self.manager.add_widget(HelloScreen())
    def build(self):
        if shaders:
            return self.root
        else:
            return self.manager
    
if __name__ == '__main__':
    RandomApp().run()