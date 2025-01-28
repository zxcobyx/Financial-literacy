from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Calculate_6jar(Screen):
    def __init__(self, **kwargs):
        super(Calculate_6jar, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Метки для отображения информации о расходах
        self.label1 = Label(text="Необходимые расходы: ")
        self.label2 = Label(text="Забота о себе: ")
        self.label3 = Label(text="Образование: ")
        self.label4 = Label(text="Копилка: ")
        self.label5 = Label(text="Инвестиции: ")
        self.label6 = Label(text="Подарки и благотворительность: ")

        # Добавление меток в макет
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.label4)
        self.layout.add_widget(self.label5)
        self.layout.add_widget(self.label6)
        
        self.add_widget(self.layout)

    def update_expenses(self, sum_1, sum_2, sum_3, sum_4, sum_5, sum_6):
        # Обновление текста меток с суммами
        self.label1.text = f"Необходимые расходы: {sum_1}"
        self.label2.text = f"Забота о себе: {sum_2}"
        self.label3.text = f"Образование: {sum_3}"
        self.label4.text = f"Копилка: {sum_4}"
        self.label5.text = f"Инвестиции: {sum_5}"
        self.label6.text = f"Подарки и благотворительность: {sum_6}"