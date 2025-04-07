from kivy.app import App
from screens.main_screen import MainScreen
from screens.profile_screen import ProfileScreen
from screens.faq import FAQScreen
from kivy.uix.screenmanager import ScreenManager, Screen

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainScreen(name='start_screen'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(FAQScreen(name='faq'))

        return sm

if __name__ == "__main__":
    MyApp().run()