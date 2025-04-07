from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from screens.const_colors import BACKGROUND_COLOR, BUTTONS_COLOR

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Основной FloatLayout для центрирования элементов
        layout = FloatLayout()

        # Вертикальный лэйаут для картинки и кнопок по центру
        center_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.5, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )

        # Горизонтальный лэйаут для картинки и кнопок
        top_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            height=150
        )

        # Картинка пользователя
        user_image = Image(
            source=r'E:\University\8 семестр\mobile\Financial-literacy\images\not_auth_user.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(None, None),
            size=(100, 100)
        )

        # Вертикальный лэйаут для кнопок
        buttons_layout = BoxLayout(
            orientation='vertical',
            size_hint=(1, 1)
        )

        # Кнопка "Авторизоваться"
        auth_button = Button(
            text="Sing in",
            background_color=BUTTONS_COLOR,
            size_hint=(1, None),
            height=60
        )

        # Кнопка "Войти"
        login_button = Button(
            text="Login",
            background_color=BUTTONS_COLOR,
            size_hint=(1, None),
            height=60
        )

        buttons_layout.add_widget(auth_button)
        buttons_layout.add_widget(login_button)

        top_layout.add_widget(user_image)
        top_layout.add_widget(buttons_layout)

        center_layout.add_widget(top_layout)

        layout.add_widget(center_layout)

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
