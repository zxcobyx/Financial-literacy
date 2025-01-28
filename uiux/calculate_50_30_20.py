from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Calculate_50_30_20(Screen):
    def __init__(self, **kwargs):
        super(Calculate_50_30_20, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Метки для отображения информации о расходах
        self.label1 = Label(text="Обязательные расходы: ")
        self.label2 = Label(text="Развлечения, хобби, путешествия: ")
        self.label3 = Label(text="Кредиты и займы: ")

        # Добавление меток в макет
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.label3)
        
        self.add_widget(self.layout)

    def update_expenses(self, sum_1, sum_2, sum_3):
        # Обновление текста меток с суммами
        self.label1.text = f"Обязательные расходы: {sum_1}"
        self.label2.text = f"Развлечения, хобби, путешествия: {sum_2}"
        self.label3.text = f"Кредиты и займы: {sum_3}"