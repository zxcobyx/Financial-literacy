from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from screens.const_colors import BACKGROUND_COLOR, BUTTONS_COLOR
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from backend.database.db_manager import create_user, check_user


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

        self.layout = FloatLayout()

        # Центральный контейнер для полей и кнопок
        self.center_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            spacing=10
        )

        # Кнопки Login и Register
        self.login_button = Button(
            text="Login",
            background_color=BUTTONS_COLOR,
            size_hint=(1, None),
            height=60
        )
        self.login_button.bind(on_press=self.show_login_fields)

        self.register_button = Button(
            text="Register",
            background_color=BUTTONS_COLOR,
            size_hint=(1, None),
            height=60
        )
        self.register_button.bind(on_press=self.show_register_fields)

        self.center_layout.add_widget(self.login_button)
        self.center_layout.add_widget(self.register_button)

        self.layout.add_widget(self.center_layout)

        # Кнопка "Назад"
        back_button = Button(
            text="Назад",
            background_color=BUTTONS_COLOR,
            size_hint=(0.3, None),
            height=50,
            pos_hint={'center_x': 0.5, 'y': 0.05}
        )
        back_button.bind(on_press=lambda inst: setattr(self.manager, 'current', 'start_screen'))
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def clear_fields(self):
        # Удаляем все элементы кроме кнопок
        self.center_layout.clear_widgets()
        self.center_layout.add_widget(self.login_button)
        self.center_layout.add_widget(self.register_button)

    def show_login_fields(self, instance):
        self.clear_fields()

        self.email_input = TextInput(hint_text='Email', size_hint=(1, None), height=40)
        self.password_input = TextInput(hint_text='Password', password=True, size_hint=(1, None), height=40)

        submit_button = Button(
            text="Войти",
            background_color=BUTTONS_COLOR,
            size_hint=(1, None),
            height=50
        )
        submit_button.bind(on_press=self.login_user)

        self.center_layout.add_widget(self.email_input)
        self.center_layout.add_widget(self.password_input)
        self.center_layout.add_widget(submit_button)

    def show_register_fields(self, instance):
        self.clear_fields()

        self.username_input = TextInput(hint_text='Username', size_hint=(1, None), height=40)
        self.email_input = TextInput(hint_text='Email', size_hint=(1, None), height=40)
        self.password_input = TextInput(hint_text='Password', password=True, size_hint=(1, None), height=40)

        submit_button = Button(
            text="Зарегистрироваться",
            background_color=BUTTONS_COLOR,
            size_hint=(1, None),
            height=50
        )
        submit_button.bind(on_press=self.register_user)

        self.center_layout.add_widget(self.username_input)
        self.center_layout.add_widget(self.email_input)
        self.center_layout.add_widget(self.password_input)
        self.center_layout.add_widget(submit_button)

    def register_user(self, instance):
        email = self.email_input.text.strip()
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        if email and username and password:
            success = create_user(email, username, password)
            if success:
                self.show_popup("Регистрация", "Пользователь успешно зарегистрирован!")
                app = App.get_running_app()
                app.current_user = username  # сохраняем пользователя
                self.manager.current = 'user_profile_screen'  # переключаемся на экран профиля
            else:
                self.show_popup("Ошибка", "Пользователь с такой почтой уже существует.")
        else:
            self.show_popup("Ошибка", "Все поля должны быть заполнены.")

    def login_user(self, instance):
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()

        if email and password:
            success = check_user(email, password)
            if success:
                self.show_popup("Вход", "Успешный вход!")
                app = App.get_running_app()
                app.current_user = email  # сохраняем текущего пользователя
                self.manager.current = 'user_profile_screen'  # переключаемся на экран профиля

                app = App.get_running_app()
                app.current_user = email

                main_screen = app.root.get_screen('start_screen')  # имя твоего экрана с кнопкой "Добавить"
                main_screen.update_add_button_state()

            else:
                self.show_popup("Ошибка", "Неверный email или пароль.")
        else:
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
