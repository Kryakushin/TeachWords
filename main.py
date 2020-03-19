from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp

class TeachWordsApp(App):
    def __init__(self, **kvargs):
        super(TeachWordsApp, self).__init__(**kvargs)

    def build(self):
        return sm

class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)

        box = BoxLayout(orientation='vertical')

        def xxx():
            return sv
        def xxb():
            return sb
        def xxn():
            return sn

        box.add_widget(Button(text='Играть', on_press=lambda x: xxx()))
        box.add_widget(Button(text='Словарь', on_press=lambda x: xxx()))
        box.add_widget(Button(text='Параметры', on_press=lambda x: xxb()))
        box.add_widget(Button(text='Поддержка', on_press=lambda x: xxn()))

        self.add_widget(box)

class PlayScreen(Screen):
    pass
class SettingsScreen(Screen):
    def Screen(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='Звук'))
        box.add_widget(Button(text='Фон(белый/чёрный)'))
        self.add_widget(box)

def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sv = ScreenManager()
sv.add_widget(PlayScreen(name='play'))
sb = ScreenManager()
sb.add_widget(SettingsScreen(name='settings'))
sn = ScreenManager()
sn.add_widget(MenuScreen(name=''))

if __name__ == '__main__':
    TeachWordsApp().run()
