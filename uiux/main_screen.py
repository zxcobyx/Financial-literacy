from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from uiux.add_dialog import AddDialog
from kivy.uix.screenmanager import Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 30])
        
        add_button = Button(
            text="Начать",
            size=(200, 50),  # Задаем фиксированный размер
            size_hint=(None, None),  # Отключаем относительный размер
            background_color=(1, 0, 0, 1),  # Устанавливаем цвет (RGB + альфа)
            pos_hint={'center_x': 0.5, 'y': 0}  # Позиция по центру
        )
        add_button.bind(on_press=self.open_dialog)

        layout.add_widget(add_button)
        self.add_widget(layout)

    def open_dialog(self, instance):
        dialog = AddDialog()
        popup = dialog.open()