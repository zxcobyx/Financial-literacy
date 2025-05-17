from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from screens.const_colors import BACKGROUND_COLOR, BUTTONS_COLOR
from backend.calculations.buckets import calculate_buckets


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
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.on_pos, size=self.on_size)

        self.layout = BoxLayout(orientation='vertical')

        self.layout.add_widget(Label(text='Давайте начнем грамотно инвестировать!', color=(0, 0, 0, 1), size_hint_y=None, height=40))

        self.data_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.data_layout.bind(minimum_height=self.data_layout.setter('height'))

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.data_layout)

        self.layout.add_widget(scroll)

        bottom_layout = ColoredBoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            height=50,
            spacing=10,
            padding=[10, 10]
        )

        profile_button = Button(text="Профиль", size_hint=(1, None), background_color=BUTTONS_COLOR)
        profile_button.bind(on_press=self.go_to_profile)

        self.add_button = Button(text="Добавить", size_hint=(1, None), background_color=BUTTONS_COLOR)
        self.add_button.bind(on_press=self.show_add_strategy_popup)

        faq_button = Button(text="FAQ", size_hint=(1, None), background_color=BUTTONS_COLOR)
        faq_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'faq'))

        bottom_layout.add_widget(profile_button)
        bottom_layout.add_widget(self.add_button)
        bottom_layout.add_widget(faq_button)

        self.layout.add_widget(bottom_layout)

        self.add_widget(self.layout)
        self.update_add_button_state()


    def update_add_button_state(self):
        app = App.get_running_app()
        if hasattr(app, 'current_user') and app.current_user:
            self.add_button.disabled = False
        else:
            self.add_button.disabled = True


    def on_pos(self, *args):
        self.rect.pos = self.pos

    def on_size(self, *args):
        self.rect.size = self.size
    
    def go_to_profile(self, instance):
        app = App.get_running_app()
        if hasattr(app, 'current_user') and app.current_user:
            # Если пользователь залогинен — переходим на экран профиля пользователя
            self.manager.current = 'user_profile_screen'
        else:
            # Если не залогинен — переходим на экран логина/регистрации
            self.manager.current = 'profile'
    
    def show_add_strategy_popup(self, instance):
        content = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        # Выбор стратегии (Spinner)
        self.strategy_spinner = Spinner(
            text='Выберите стратегию',
            values=('Buckets',),  # Можно добавить другие, если будут
            size_hint=(1, None),
            height=44
        )

        content.add_widget(self.strategy_spinner)

        # Ввод суммы
        self.amount_input = TextInput(
            hint_text='Введите сумму',
            input_filter='float',
            multiline=False,
            size_hint=(1, None),
            height=44
        )
        content.add_widget(self.amount_input)

        # Кнопка "Добавить"
        add_btn = Button(text='Добавить', size_hint=(1, None), height=44)
        add_btn.bind(on_press=self.on_add_strategy)
        content.add_widget(add_btn)

        self.popup = Popup(title='Добавить стратегию',
                           content=content,
                           size_hint=(0.8, 0.5),
                           auto_dismiss=True)
        self.popup.open()

    def on_add_strategy(self, instance):
        strategy = self.strategy_spinner.text
        amount_text = self.amount_input.text.strip()

        if strategy == 'Выберите стратегию' or not amount_text:
            # Можно показать ошибку, например, через popup
            self.show_error("Пожалуйста, выберите стратегию и введите сумму.")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            self.show_error("Некорректная сумма.")
            return

        if strategy == "Buckets":
            results = calculate_buckets(amount)
        else:
            self.show_error("Стратегия не реализована.")
            return

        self.add_strategy_result(strategy, amount, results)
        self.popup.dismiss()

    def add_strategy_result(self, strategy, amount, results):
        # Заголовок стратегии и суммы
        header = Label(text=f"Стратегия: {strategy}\nСумма: {amount}", size_hint_y=None, height=60, color=(0, 0, 0, 1))
        self.data_layout.add_widget(header)

        # Предполагаем, что results — словарь, где ключ — название пункта, значение — сумма
        for key, value in results.items():
            lbl = Label(text=f"{key}: {value:.2f}", size_hint_y=None, height=30, color=(0, 0, 0, 1))
            self.data_layout.add_widget(lbl)

        # Добавим разделитель (пустой лейбл с фиксированной высотой)
        self.data_layout.add_widget(Label(size_hint_y=None, height=20))



    def show_error(self, message):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button

        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        btn = Button(text="Закрыть", size_hint=(1, 0.3))
        content.add_widget(btn)

        popup = Popup(title="Ошибка", content=content, size_hint=(0.6, 0.4), auto_dismiss=False)
        btn.bind(on_release=popup.dismiss)
        popup.open()
