from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from uiux.add_dialog import AddDialog

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        add_button = Button(text='Добавить', size_hint_y=None, height=40)
        add_button.bind(on_press=self.open_dialog)
        self.add_widget(add_button)

    def open_dialog(self, instance):
        dialog = AddDialog()
        popup = dialog.open()
