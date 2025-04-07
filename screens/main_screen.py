from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from screens.const_colors import BACKGROUND_COLOR, BUTTONS_COLOR

class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ColoredBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Основной вертикальный лэйаут
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Давайте начнем грамотно инвестировать!', color=(0, 0, 0, 1)))
        
        # Нижний горизонтальный лэйаут для кнопок навигации
        bottom_layout = ColoredBoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            height=50,
            spacing=10,
            padding=[10, 10]
        )

        # Кнопка "Профиль"
        profile_button = Button(
            text="Профиль",
            size_hint=(1, None),
            background_color=BUTTONS_COLOR
        )
        profile_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'profile'))

        # Кнопка "Добавить"
        add_button = Button(
            text="Добавить",
            size_hint=(1, None),
            background_color=BUTTONS_COLOR
        )
        add_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'menu'))

        # Кнопка "FAQ"
        faq_button = Button(
            text="FAQ",
            size_hint=(1, None),
            background_color=BUTTONS_COLOR
        )
        faq_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'faq'))

        # Добавляем кнопки в нижний лэйаут
        bottom_layout.add_widget(profile_button)
        bottom_layout.add_widget(add_button)
        bottom_layout.add_widget(faq_button)

        # Добавляем нижний лэйаут в основной лэйаут
        layout.add_widget(bottom_layout)
        
        self.add_widget(layout)

    def on_pos(self, *args):
        self.rect.pos = self.pos

    def on_size(self, *args):
        self.rect.size = self.size