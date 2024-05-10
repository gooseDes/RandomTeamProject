from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.core.window import Window

class AutoLabel(MDLabel):
    def __init__(self, font_hint=1, font_hint_by='x', font='arial', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_hint = font_hint
        self.font_hint_by = font_hint_by
        self.font = font
        self.theme_text_color='Custom'
        Clock.schedule_interval(self.update, 1/30)
    def update(self, dt):
        self.font_name=self.font
        if self.font_hint_by == 'x':
            self.font_size = Window.size[0]*self.font_hint
        elif self.font_hint_by == 'y':
            self.font_size = Window.size[1]*self.font_hint
        self.text_size=[Window.size[0]*self.size_hint_x, Window.size[1]*self.size_hint_y]