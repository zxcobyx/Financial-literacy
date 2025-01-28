from kivy.app import App
from uiux.main_screen import MainScreen

class MyApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    MyApp().run()
