from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 30])
        
        start_button = Button(
            text="Начать",
            size=(200, 50),  # Задаем фиксированный размер
            size_hint=(None, None),  # Отключаем относительный размер
            background_color=(1, 0, 0, 1),  # Устанавливаем цвет (RGB + альфа)
            pos_hint={'center_x': 0.5, 'y': 0}  # Позиция по центру
        )
        start_button.bind(on_press=self.on_start_button_press)
        
        layout.add_widget(start_button)
        self.add_widget(layout)

    def on_start_button_press(self, instance):
        self.manager.current = 'second'
        # Здесь можно добавить логику для перехода на другой экран или выполнения действия

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 30])
        back_button = Button(
            text="Вернуться",
            size=(200, 50),  # Задаем фиксированный размер
            size_hint=(None, None),  # Отключаем относительный размер
            background_color=(1, 0, 0, 1),  # Устанавливаем цвет (RGB + альфа)
            pos_hint={'center_x': 0.5, 'y': 0}  # Позиция по центру
        )
        back_button.bind(on_press=self.go_to_main)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main'  # Переход на главный экран

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        return sm

if __name__ == "__main__":
    MyApp().run()