from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from widgets import AutoLabel

class HelloScreen(MDScreen):
    name = StringProperty('hello')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title=AutoLabel(text="Ласкаво Просимо до [name here]!", font_hint_by='x', font_hint=0.07, font='assets/fonts/ComicRelief', text_color='3479ad', size_hint=[0.8,0.4], pos_hint={'center_x':0.5, 'center_y':0.75}, halign='center', valign='center', bold=True, outline_width=4, outline_color='ffffff')
        self.add_widget(self.title)