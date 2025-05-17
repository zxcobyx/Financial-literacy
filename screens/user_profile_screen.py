from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from screens.const_colors import BACKGROUND_COLOR, BUTTONS_COLOR


class UserProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(UserProfileScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.user_label = Label(text='Пользователь: ', font_size=24, color=(0, 0, 0, 1))
        self.layout.add_widget(self.user_label)

        btn_logout = Button(text='Выйти', size_hint=(1, None), height=50, background_color=BUTTONS_COLOR)
        btn_logout.bind(on_press=self.logout)

        btn_back = Button(text='Назад', size_hint=(1, None), height=50, background_color=BUTTONS_COLOR)
        btn_back.bind(on_press=self.go_back)

        self.layout.add_widget(btn_logout)
        self.layout.add_widget(btn_back)

        self.add_widget(self.layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_pre_enter(self, *args):
        app = self.manager.app
        current_user = getattr(app, 'current_user', None)
        if current_user:
            self.user_label.text = f'Пользователь: {current_user}'
        else:
            self.user_label.text = 'Пользователь: Неизвестен'

    def logout(self, instance):
        app = self.manager.app
        app.current_user = None
        self.manager.current = 'profile'

    def go_back(self, instance):
        self.manager.current = 'start_screen'
