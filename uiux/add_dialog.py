from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from uiux.calculate_50_30_20 import Calculate_50_30_20
from uiux.calculate_6jar import Calculate_6jar

class AddDialog(BoxLayout):
    def __init__(self, **kwargs):
        super(AddDialog, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.income_input = TextInput(hint_text='Введите доход', size_hint_y=None, height=40)
        self.add_widget(self.income_input)

        self.method_spinner = Spinner(
            text='6 кувшинов',
            values=['6 кувшинов', '50/30/20'],
            size_hint_y=None, height=40
        )
        self.add_widget(self.method_spinner)

        self.calculate_button = Button(text='Рассчитать', size_hint_y=None, height=40)
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)

    def open(self):
        popup = Popup(title='Добавить', content=self, size_hint=(None, None), size=(300, 200))
        popup.open()
        return popup

    def calculate(self, instance):
        try:
            income = float(self.income_input.text)
            method = self.method_spinner.text

            if method == '6 кувшинов':
                result = calculate_buckets(income)
            elif method == '50/30/20':
                result = calculate_budget(income)

            result_text = '\n'.join(f"{key}: {value:.2f}" for key, value in result.items())
            popup = Popup(title='Результат', content=Label(text=result_text), size_hint=(None, None), size=(400, 400))
            popup.open()
        except ValueError:
            popup = Popup(title='Ошибка', content=Label(text='Неправильный формат дохода'), size_hint=(None, None), size=(200, 100))
            popup.open()