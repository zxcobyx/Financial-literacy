from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from screens.const_colors import BACKGROUND_COLOR, BUTTONS_COLOR
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from backend.database.db_manager import create_user, check_user

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        from kivy.uix.textinput import TextInput
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

        # Поля ввода email, username, password
        self.email_input = TextInput(hint_text='Email', size_hint=(1, None), height=40)
        self.username_input = TextInput(hint_text='Username', size_hint=(1, None), height=40)
        self.password_input = TextInput(hint_text='Password', password=True, size_hint=(1, None), height=40)

        center_layout.add_widget(self.email_input)
        center_layout.add_widget(self.username_input)
        center_layout.add_widget(self.password_input)

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
        auth_button.bind(on_press=self.register_user)


        # Кнопка "Войти"
        login_button = Button(
            text="Login",
            background_color=BUTTONS_COLOR,
            size_hint=(1, None),
            height=60
        )
        login_button.bind(on_press=self.login_user)


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

    def register_user(self, instance):
        email = self.email_input.text.strip()
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        if email and username and password:
            success = create_user(email, username, password)
            if success:
                print("Пользователь успешно зарегистрирован!")
                self.show_popup("Регистрация", "Пользователь успешно зарегистрирован!")
            else:
                print("Ошибка: пользователь с такой почтой уже существует.")
                self.show_popup("Ошибка", "Пользователь с такой почтой уже существует.")
        else:
            print("Все поля должны быть заполнены.")
            self.show_popup("Ошибка", "Все поля должны быть заполнены.")

    def login_user(self, instance):
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()

        if email and password:
            success = check_user(email, password)
            if success:
                print("Успешный вход!")
                self.show_popup("Вход", "Успешный вход!")
            else:
                print("Неверный email или пароль.")
                self.show_popup("Ошибка", "Неверный email или пароль.")
        else:
            print("Введите email и пароль.")
            self.show_popup("Ошибка", "Введите email и пароль.")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        btn_close = Button(text='Закрыть', size_hint=(1, 0.3))
        content.add_widget(btn_close)

        popup = Popup(title=title,
                    content=content,
                    size_hint=(0.7, 0.4),
                    auto_dismiss=False)
        btn_close.bind(on_release=popup.dismiss)
        popup.open()