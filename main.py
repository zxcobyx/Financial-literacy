from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.main_screen import MainScreen
from screens.profile_screen import ProfileScreen
from screens.faq import FAQScreen
from screens.user_profile_screen import UserProfileScreen


class MyApp(App):
    def build(self):
        self.current_user = None

        sm = ScreenManager()
        sm.app = self

        sm.add_widget(MainScreen(name='start_screen'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(FAQScreen(name='faq'))
        sm.add_widget(UserProfileScreen(name='user_profile_screen'))

        return sm


if __name__ == "__main__":
    MyApp().run()
