from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from screens.const_colors import BUTTONS_COLOR, BACKGROUND_COLOR

class FAQScreen(Screen):
    def __init__(self, **kwargs):
        super(FAQScreen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Это экран FAQ", color=(0, 0, 0, 1)))

        # Лэйаут для кнопки "Назад" внизу
        bottom_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            height=50,
            pos_hint={'center_x': 0.5, 'y': 0}
        )

        # Кнопка "Назад"
        back_button = Button(
            text="Назад",
            background_color=BUTTONS_COLOR,
            size_hint=(1, None),
            height=50
        )
        back_button.bind(on_press=lambda instanse: setattr(self.manager, 'current', 'start_screen'))
        
        bottom_layout.add_widget(back_button)
        layout.add_widget(bottom_layout)
        self.add_widget(layout)

    def on_pos(self, *args):
        self.rect.pos = self.pos

    def on_size(self, *args):
        self.rect.size = self.size